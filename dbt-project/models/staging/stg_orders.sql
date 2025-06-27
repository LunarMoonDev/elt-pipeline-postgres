/*
    Purpose: This model is used to stage the orders data from the landing zone.
    Source: orders
    Notes: includes a case statement to convert status codes to descriptive text
*/

{{ config(
    materialized='incremental',
    unique_key='OrderId',
    tags=['incremental', 'daily']
) }}

select
    OrderId::integer as OrderId,
    OrderDate::date as OrderDate,
    CustomerId::varchar as CustomerId,
    EmployeeId::integer as EmployeeId,
    StoreId::integer as StoreId,
    Status::varchar as StatusCD,
    case
        when Status = '01' then 'In Progress'
        when Status = '02' then 'Completed'
        when Status = '03' then 'Cancelled'
        else NULL
    end as StatusDesc,
    case
        when StoreId = 1000 then 'Online'
        else 'In-Store'
    end as order_channel,
    Updated_at::timestamp as Updated_at,
    current_timestamp as dbt_updated_at
from {{ source('landing', 'orders') }}

{% if is_incremental() %}
where Updated_at >= (select max(dbt_updated_at) from {{ this }})
{% endif %}
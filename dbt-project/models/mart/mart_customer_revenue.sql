/*
    Purpose: This model calculates the total revenue and order count per customer.
    Source: int_orders_fact, stg_customers
    Notes: Aggregates order data to provide insights into customer revenue and order counts.
*/

{{ config(materialized='table') }}

select
    os.CustomerId::varchar as CustomerId,
    c.CustomerName::varchar as CustomerName,
    SUM(os.OrderCount)::decimal as OrderCount,
    SUM(os.Revenue)::decimal as Revenue
from
    {{ ref('int_orders_fact') }} as os
join
    {{ ref('stg_customers') }} as c
    on os.CustomerId = c.CustomerId
group by
    os.CustomerId,
    c.CustomerName
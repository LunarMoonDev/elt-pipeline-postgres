/*
    Purpose: This model is used to stage the customers data from the landing zone.
    Source: customers
    Notes: this is for demonstrating snapshot feature
*/

{% snapshot customers_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='CustomerId',
        strategy='timestamp',
        updated_at='Updated_at'
    )
}}

select
    CustomerId::varchar as CustomerId,
    FirstName::varchar as FirstName,
    LastName::varchar as LastName,
    Email::varchar as Email,
    Phone::varchar as Phone,
    Address::varchar as Address,
    City::varchar as City,
    State::varchar as State,
    ZipCode::varchar as ZipCode,
    Updated_at::timestamp as Updated_at,
    FirstName::varchar || ' ' || LastName::varchar as CustomerName
from {{ source('landing', 'customers') }}

{% endsnapshot %}
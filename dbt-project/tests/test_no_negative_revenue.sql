/*
    Purpose: grabs the negative revenue from orders_fact
    Source: int_orders_fact
    Notes: negative revenue must not exist
*/

select
    OrderId
from
    {{ ref('int_orders_fact') }}
where
    Revenue < 0
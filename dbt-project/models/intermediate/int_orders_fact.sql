/*
    Purpose: This model aggregates order data to create fact for customer revenue
    Source: stg_orders, stg_orderitems, stg_customers
    Notes: This model joins orders with order items and customers, aggregates revenue, and counts distinct orders.
*/
{{ config(materialized='table') }}

select
    o.OrderId::integer as OrderId,
    o.OrderDate::date as OrderDate,
    o.CustomerId::varchar as CustomerId,
    o.EmployeeId::integer as EmployeeId,
    o.StoreId::integer as StoreId,
    o.StatusCD::varchar as StatusCD,
    o.StatusDesc::varchar as StatusDesc,
    COUNT(DISTINCT o.OrderId)::integer as OrderCount,
    SUM(oi.TotalPrice)::decimal as Revenue,
    o.Updated_at::timestamp as Updated_at
from 
    {{ ref('stg_orders') }} as o
join 
    {{ ref('stg_orderitems') }} as oi
    on o.OrderId = oi.OrderId
group by 
    o.OrderId, 
    o.OrderDate, 
    o.CustomerId,
    o.EmployeeId, 
    o.StoreId, 
    o.StatusCD, 
    o.StatusDesc, 
    o.Updated_at
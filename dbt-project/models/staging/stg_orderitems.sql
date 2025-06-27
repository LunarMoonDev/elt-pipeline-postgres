/*
    Purpose: This model is used to stage the order items data from the landing zone.
    Source: orderitems
    Notes: calculates the total price for each order item by multiplying quantity and unit price
*/

select
    OrderItemID::INTEGER AS OrderItemID,
    OrderId::INTEGER AS OrderId,
    ProductID::INTEGER AS ProductID,
    Quantity::INTEGER AS Quantity,
    UnitPrice::DECIMAL AS UnitPrice,
    (Quantity::INTEGER * UnitPrice::DECIMAL) AS TotalPrice,
    Updated_at::TIMESTAMP AS Updated_at
from {{ source('landing', 'orderitems') }}
{{  dbt_utils.deduplicate(
        relation = ref("stg_orderitems"),
        partition_by = 'OrderId',
        order_by = 'Updated_at desc'
    )
}}
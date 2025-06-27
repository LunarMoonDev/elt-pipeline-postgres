{% set expected_counts = {
    'customers': 5,
    'orders': 5,
    'orderitems': 5,
    'employees': 5
} %}


{% for table, expected_count in expected_counts.items() %}
    select '{{ table }}' as table_name,
            (select count(*) from {{ source('landing', table) }}) as record_count,
            {{ expected_count }} as expected_count
    where (select count(*) from {{ source('landing', table) }}) < {{ expected_count }}
    {% if not loop.last %} union all {% endif %}
{% endfor %}
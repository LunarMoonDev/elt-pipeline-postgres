/*
    Test: string_not_empty
    Purpose: Checks if a given column is not empty for a given model
    Arguments:
        model: model or table to test
        column_name: column to check
*/

{% test string_not_empty(model, column_name) %}
    select {{ column_name }}
    from {{ model }}
    where trim({{ column_name }}) = ''
{% endtest %}
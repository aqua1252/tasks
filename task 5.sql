update parents
set has_children = false
where id not in(
    select distinct parent_id
    from children
    );

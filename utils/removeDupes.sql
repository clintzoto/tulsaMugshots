select bad_rows.*
from newdevrecords as bad_rows
   inner join (
      select personId, MIN(inc) as min_id
      from newdevrecords
      group by personId
      having count(*) > 1
   ) as good_rows on good_rows.personId = bad_rows.personId
      and good_rows.min_id <> bad_rows.inc


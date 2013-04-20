Title: Clean a PostgreSQL database directory
Date: 2008-09-11 14:52
Author: James
Tags: Tips
Slug: clean-postgres-databas

After building a database using an ill-judged algorithm, I ended up with
junk in the database that consumed 600MB of space in the Postgres data
directory. Deleting the bad data did not free this space immediately,
and I was too impatient to wait for the auto vacuuming to kick in.

Here are the steps I took to clean up the database and data directory --
with extreme prejudice.

In the psql console:

    :::text
    VACUUM FULL VERBOSE;
    REINDEX DATABASE mydatabase;

On the command line:

    :::console
    pg_resetxlog /path/to/my/datadir

Running all of these steps is a brutal process. Do not run the `pg_resetxlog`
command if you have important data, because you will probably want to keep your
[write ahead log][].

  [write ahead log]: http://www.postgresql.org/docs/8.1/static/backup-online.html

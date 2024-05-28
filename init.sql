-- Table: public.pages

-- DROP TABLE IF EXISTS public.pages;

CREATE TABLE pages
(
    id serial NOT NULL PRIMARY KEY,
    path text  NOT NULL,
    url text  NOT NULL,
    html text ,
    text text ,
    created_at date NOT NULL DEFAULT CURRENT_DATE

)

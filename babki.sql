--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Debian 15.1-1.pgdg110+1)
-- Dumped by pg_dump version 15.1 (Debian 15.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO babki;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.categories (
    "ID" uuid NOT NULL,
    title character varying NOT NULL,
    parrent_category uuid
);


ALTER TABLE public.categories OWNER TO babki;

--
-- Name: drink_ingridients; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.drink_ingridients (
    "ID" uuid NOT NULL,
    blurb character varying NOT NULL,
    drink_id uuid,
    ingridient_id uuid
);


ALTER TABLE public.drink_ingridients OWNER TO babki;

--
-- Name: drinks; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.drinks (
    "ID" uuid NOT NULL,
    title character varying NOT NULL,
    is_active_constructor boolean DEFAULT true NOT NULL
);


ALTER TABLE public.drinks OWNER TO babki;

--
-- Name: ingridients; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.ingridients (
    "ID" uuid NOT NULL,
    title character varying NOT NULL
);


ALTER TABLE public.ingridients OWNER TO babki;

--
-- Name: params_ingridients; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.params_ingridients (
    "ID" uuid NOT NULL,
    params_id uuid,
    ingridient_id uuid
);


ALTER TABLE public.params_ingridients OWNER TO babki;

--
-- Name: values_for_ingridients; Type: TABLE; Schema: public; Owner: babki
--

CREATE TABLE public.values_for_ingridients (
    "ID" uuid NOT NULL,
    title character varying NOT NULL,
    is_default boolean
);


ALTER TABLE public.values_for_ingridients OWNER TO babki;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.alembic_version (version_num) FROM stdin;
61b9b2c98ed9
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.categories ("ID", title, parrent_category) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa6	string	3fa85f64-5717-4562-b3fc-2c963f66afa6
3fa85f64-5717-4562-b3fc-2c963f66afa2	string	3fa85f64-5717-4562-b3fc-2c963f66afa6
\.


--
-- Data for Name: drink_ingridients; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.drink_ingridients ("ID", blurb, drink_id, ingridient_id) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1
3fa85f64-5717-4562-b3fc-2c963f66afa2	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa2
3fa85f64-5717-4562-b3fc-2c963f66afa3	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa3
3fa85f64-5717-4562-b3fc-2c963f66afa4	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa4
\.


--
-- Data for Name: drinks; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.drinks ("ID", title, is_active_constructor) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa1	капучино	t
3fa85f64-5717-4562-b3fc-2c963f66afa2	фильтр	t
3fa85f64-5717-4562-b3fc-2c963f66afa3	раф	t
3fa85f64-5717-4562-b3fc-2c963f66afa4	флэт уайт	t
3fa85f64-5717-4562-b3fc-2c963f66afa5	лате	t
3fa85f64-5717-4562-b3fc-2c963f66afa6	Какао	t
3fa85f64-5717-4562-b3fc-2c963f66afa7	Матча латте	t
\.


--
-- Data for Name: ingridients; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.ingridients ("ID", title) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa1	эспрессо
3fa85f64-5717-4562-b3fc-2c963f66afa2	молоко
3fa85f64-5717-4562-b3fc-2c963f66afa3	температура
3fa85f64-5717-4562-b3fc-2c963f66afa4	сиропы
3fa85f64-5717-4562-b3fc-2c963f66afa5	фильтр
3fa85f64-5717-4562-b3fc-2c963f66afa6	вода
3fa85f64-5717-4562-b3fc-2c963f66afa7	Размер
3fa85f64-5717-4562-b3fc-2c963f66afa8	Какао
3fa85f64-5717-4562-b3fc-2c963f66afa9	Матча
\.


--
-- Data for Name: params_ingridients; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.params_ingridients ("ID", params_id, ingridient_id) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa3	3fa85f64-5717-4562-b3fc-2c963f66afa3	3fa85f64-5717-4562-b3fc-2c963f66afa1
3fa85f64-5717-4562-b3fc-2c963f66afa2	3fa85f64-5717-4562-b3fc-2c963f66afa2	3fa85f64-5717-4562-b3fc-2c963f66afa1
3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1	3fa85f64-5717-4562-b3fc-2c963f66afa1
\.


--
-- Data for Name: values_for_ingridients; Type: TABLE DATA; Schema: public; Owner: babki
--

COPY public.values_for_ingridients ("ID", title, is_default) FROM stdin;
3fa85f64-5717-4562-b3fc-2c963f66afa3	покрепче	f
3fa85f64-5717-4562-b3fc-2c963f66afa2	стандарт	t
3fa85f64-5717-4562-b3fc-2c963f66afa1	без кофеина	f
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY ("ID");


--
-- Name: drink_ingridients drink_ingridients_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.drink_ingridients
    ADD CONSTRAINT drink_ingridients_pkey PRIMARY KEY ("ID");


--
-- Name: drinks drinks_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.drinks
    ADD CONSTRAINT drinks_pkey PRIMARY KEY ("ID");


--
-- Name: ingridients ingridients_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.ingridients
    ADD CONSTRAINT ingridients_pkey PRIMARY KEY ("ID");


--
-- Name: params_ingridients params_ingridients_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.params_ingridients
    ADD CONSTRAINT params_ingridients_pkey PRIMARY KEY ("ID");


--
-- Name: values_for_ingridients values_for_ingridients_pkey; Type: CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.values_for_ingridients
    ADD CONSTRAINT values_for_ingridients_pkey PRIMARY KEY ("ID");


--
-- Name: ix_categories_parrent_category; Type: INDEX; Schema: public; Owner: babki
--

CREATE INDEX ix_categories_parrent_category ON public.categories USING btree (parrent_category);


--
-- Name: categories categories_parrent_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_parrent_category_fkey FOREIGN KEY (parrent_category) REFERENCES public.categories("ID");


--
-- Name: drink_ingridients drink_ingridients_drink_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.drink_ingridients
    ADD CONSTRAINT drink_ingridients_drink_id_fkey FOREIGN KEY (drink_id) REFERENCES public.drinks("ID");


--
-- Name: drink_ingridients drink_ingridients_ingridient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.drink_ingridients
    ADD CONSTRAINT drink_ingridients_ingridient_id_fkey FOREIGN KEY (ingridient_id) REFERENCES public.ingridients("ID");


--
-- Name: params_ingridients params_ingridients_ingridient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.params_ingridients
    ADD CONSTRAINT params_ingridients_ingridient_id_fkey FOREIGN KEY (ingridient_id) REFERENCES public.ingridients("ID");


--
-- Name: params_ingridients params_ingridients_params_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: babki
--

ALTER TABLE ONLY public.params_ingridients
    ADD CONSTRAINT params_ingridients_params_id_fkey FOREIGN KEY (params_id) REFERENCES public.values_for_ingridients("ID");


--
-- PostgreSQL database dump complete
--


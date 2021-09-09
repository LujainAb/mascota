--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

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
-- Name: pet; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pet (
    id integer NOT NULL,
    name character varying(50),
    type character varying(50),
    breed character varying(50),
    sex character varying(50),
    age integer,
    behaviour character varying(50)
);


--
-- Name: pet_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.pet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: pet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.pet_id_seq OWNED BY public.pet.id;


--
-- Name: shelter; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.shelter (
    id integer NOT NULL,
    name character varying(50),
    city character varying(50)
);


--
-- Name: shelter_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.shelter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: shelter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.shelter_id_seq OWNED BY public.shelter.id;


--
-- Name: pet id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pet ALTER COLUMN id SET DEFAULT nextval('public.pet_id_seq'::regclass);


--
-- Name: shelter id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.shelter ALTER COLUMN id SET DEFAULT nextval('public.shelter_id_seq'::regclass);


--
-- Data for Name: pet; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pet (id, name, type, breed, sex, age, behaviour) FROM stdin;
1	Bella	Cat	british longhair	female	2	needy and scratchs alot
2	cloud	Cat	scottish	male	1	playful and lovely
5	Cody	Dog	German shepard	male	3	very quite
3	Cody edit	\N	\N	\N	5	\N
\.


--
-- Data for Name: shelter; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.shelter (id, name, city) FROM stdin;
1	pet hun	Riyadh
\.


--
-- Name: pet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pet_id_seq', 6, true);


--
-- Name: shelter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.shelter_id_seq', 1, false);


--
-- Name: pet pet_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_pkey PRIMARY KEY (id);


--
-- Name: shelter shelter_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.shelter
    ADD CONSTRAINT shelter_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


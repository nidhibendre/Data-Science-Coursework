-- CS3200: Database Design
-- GAD: The Genetic Association Database
show variables where variable_name like '%local%';
set global local_infile=ON;

drop database if exists gad;
create database gad;

drop table if exists gad;

CREATE TABLE gad (
  gad_id int,
  association text,
  phenotype text,
  disease_class text,
  chromosome text,
  chromosome_band text,
  dna_start int,
  dna_end int,
  gene text,
  gene_name text,
  reference text,
  pubmed_id int,
  year int,
  population text
);

LOAD DATA LOCAL 
INFILE '/Users/nidhibendre/Documents/cs3200/data/gad.csv'
INTO TABLE gad
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
IGNORE 1 ROWS;

use gad;


-- Exploration:
-- 1. 
-- Explore the content of the various columns in your gad table.
select * from gad;
-- List all genes that are "G protein-coupled" receptors in alphabetical order by gene symbol
select gene, gene_name, chromosome from gad
where gene_name like '%G protein-coupled%'
order by gene;


-- 2. 
-- How many records are there for each disease class?
 select disease_class, count(*) as 'frequency'
 from gad
 group by disease_class
 order by frequency desc;
 

-- 3. 
-- List all distinct phenotypes related to the disease class "IMMUNE"
select distinct phenotype 
from gad
where disease_class = "IMMUNE"
order by phenotype;


-- 4.
-- Show the immune-related phenotypes
-- based on the number of records reporting a positive association with that phenotype.
-- Display both the phenotype and the number of records with a positive association
-- Only report phenotypes with at least 60 records reporting a positive association.
-- Your list should be sorted in descending order by number of records
-- Use a column alias: "num_records"
select phenotype, count(*) as 'num_records'
from gad
where disease_class = 'IMMUNE' and association = 'Y'
group by phenotype
having num_records >= 60
order by num_records desc;


-- 5.
-- List the gene symbol, gene name, and chromosome attributes related
-- to genes positively linked to asthma (association = Y).
-- Include in your output any phenotype containing the substring "asthma"
-- List each distinct record once
-- Sort  gene symbol
select distinct gene, gene_name, chromosome, chromosome_band
from gad
where phenotype like '%asthma%' and association = 'Y'
order by gene;


-- 6. 
-- For each chromosome, over what range of nucleotides do we find
-- genes mentioned in GAD?
-- Exclude cases where the dna_start value is 0 or where the chromosome is unlisted.
-- Sort your data by chromosome. Don't be concerned that
-- the chromosome values are TEXT. (1, 10, 11, 12, ...)
select chromosome, 
		min(dna_start) as min_range, 
		max(dna_end) as max_range
from gad 
where not dna_start = 0 and not chromosome = ''
group by chromosome
order by chromosome; 
 

-- 7 
-- For each gene, what is the earliest and latest reported year
-- involving a positive association
-- Ignore records where the year isn't valid. (Explore the year column to determine what constitutes a valid year.)
-- Output the gene, min-year, max-year, and number of GAD records
-- order from most records to least.
-- Columns with aggregation functions should be aliased
select gene, 
	   min(year) as 'min_year',
       max(year) as 'max_year',
       count(*) as 'num_gad_records'
from gad
where association = 'Y' and not year = 0
group by gene
order by num_gad_records desc;


-- 8. 
-- Which genes have a total of at least 100 positive association records (across all phenotypes)?
-- Give the gene symbol, gene name, and the number of associations
-- Use a 'num_records' alias in your query wherever possible
select gene, gene_name, count(*) as 'num_records'
from gad
where association = 'Y' 
group by gene, gene_name
having num_records >= 100;



-- 9. 
-- How many total GAD records are there for each population group?
-- Sort in descending order by count
-- Show only the top five results based on number of records
-- Do NOT include cases where the population is blank
select population, count(*) as 'num_records'
from gad
where not population = ''
group by population
order by num_records desc
limit 5;


-- 10. 
-- In question 5, we found asthma-linked genes
-- But these genes might also be implicated in other diseases
-- Output gad records involving a positive association between ANY asthma-linked gene and ANY disease/phenotype
-- Sort your output alphabetically by phenotype
-- Output the gene, gene_name, association (should always be 'Y'), phenotype, disease_class, and population
-- Hint: Use a subselect in your WHERE class and the IN operator
select distinct gene, gene_name, association, phenotype, disease_class, population
from gad
where association = 'Y' and
gene in
	(select gene
     from gad
     where phenotype like '%asthma%' and association = 'Y')
order by phenotype;


-- 11. 
-- Modify your previous query.
-- Let's count how many times each of these asthma-gene-linked phenotypes occurs
-- in our output table produced by the previous query.
-- Output just the phenotype, and a count of the number of occurrences for the top 5 phenotypes
-- with the most records involving an asthma-linked gene (EXCLUDING asthma itself).
select phenotype, count(*) as 'num_records'
from gad
where association = 'Y' and not phenotype like '%asthma%' and 
gene in
	(select gene
     from gad
     where phenotype like '%asthma%'and association = 'Y')
group by phenotype
order by num_records desc
limit 5;


-- 12. 
-- Interpret your analysis

-- a) Search the Internet. Does existing biomedical research support a connection between asthma and the
-- top phenotype you identified above? Cite some sources and justify your conclusion!

-- The connection between asthma and type 1 diabetes phenotype has been explored before. Studies have found that 
-- siblings of people with asthma had an increased risk of type 1 diabetes and vice versa, but scientists are unsure of the reason
-- behind this connection. One hypothesis is that systematic inflammation can increase the risk of both. 
-- Sources:
-- https://www.medicalnewstoday.com/articles/diabetes-and-asthma#asthma-risk-factors
-- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616625/#
-- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8198343/

-- b) Why might a drug company be interested in instances of such "overlapping" phenotypes?
-- Drug companies can optimize their results by trying to target both asthma and diabetes 1 with one intervention 
-- to save time and resources and lead to greater profits as it opens up the drug to be used by a greater population. 




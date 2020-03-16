# Text Analysis with NLP

## Instructions

* We suggest to use the Spacy NLP library as a baseline and import additional packages as needed. But feel free to use something else if you feel it gives a better result.
* Please structure and document your code, so we can follow your thought process.
* Please use git and push code changes on a frequent basis to a private project. You can fork the initial repository to get started.
* We're interested in the quality of the technical solution, but also how easy it is to work with you.
* We're also interested if you can improve on the suggested solution below or uncover aspects/approaches that we may not have considered.

## Sample text

### Roles

#### Role 1
* Understand customer needs and develop high-quality presentations, proposals and software demonstrations that speak to these needs – building a consensus for change on a multi-stakeholder basis
* Work with the Enterprise sales team to build, manage and maintain customer relationships
* Provide pre-sales technical assistance to members of the sales team to ensure proper technical and business fit
* Work with marketing on new product development
* Present professional and personalised demos
* Need to ensure prospective customers are aligned technically with the sales process
* Need to understand and demonstrate the solution and how to integrate to other business systems

#### Role 2

Must Have:

* Experience shaping the BI strategy from C-Level to Technical developers.
* Extensive delivery of platform within a Business Intelligence and Analytics function.
* Communication with stakeholders on all levels.
* Understanding and experience within KPIs, identifying data sources, building a visualization map and dashboarding.
* Led and built a Business Intelligence function and team.
* Background within Utilities, Energy, Oil & Gas.

#### Role 3

Key Responsibilities

* Lead customers in the creation of new digital solutions which foster their competitive advantage
* Enhance and build digital transformation roadmaps
* Link digital capabilities to our clients business strategy
* Develop C-suite and line-of-business relationships within the customer organization
* Define, guide and implement innovation programs – governance, portfolio mix and business fit
* Establish the use of cloud services as a means to drive innovation
* Collaborate with other AWS specialist teams to drive and shape solutions to accelerate our customer’s business outcomes


Basic Qualifications

* Experience with a major consulting firm or experience in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies.
* Experience in two or more of the following transformation practice areas: ERP (business process architecture and solution implementation), business case and use case development, financial modelling, BI and Analytics strategy and implementation, complex program management, enterprise business / process / IT architectures, executive agenda items and metrics.
* Broad understanding of how businesses operate and compete and an understanding of the relationship between major functional areas of the product-centric enterprise (design, plan, procure, manufacture, distribute, service).
* Ability to analyse financial and operational data and synthesize findings in common business language.
* Experience in using Design Thinking Principles to structure a customer’s thinking and flush out innovative concepts.
* Deep understanding of change management practices, particularly stakeholder analysis, workforce readiness and leadership communications.
* Strong background in one of the following methodologies: Sigma, Agile/SCRUM, SAFe
* Understanding of modern cloud delivery models (Public, Private and Hybrid).
* Great business writing and presentation skills.
* Excellent communication skills in English
* This is a customer facing role. You will be required to travel to client locations to deliver professional services as needed

Preferred Qualifications

* Broad understanding of enterprise systems in large organizations and trends in cloud applications, system integration, and mobile technologies.
* Excellent program management skills including developing project plans, resourcing and budgeting projects, and managing a disciplined execution methodology with both internal (direct) and external (indirect) team members.
* Experience implementing one or more enterprise solutions on premise and/or in the cloud: ERP, PLM, IoT / Connected Products or Operations, Supply Chain functions as specified above.
* Passion for helping customers transform using cloud technologies.

### Resume

Consulting customer lead, Company 1 – San Jose (CR), Toronto (CA)
January 2018 - May 2018
* Identified processes automation portfolio totalling 50 FTE for 2019 and long-term potential of 200+ FTE
* Oversaw agile delivery of four opportunities, working with offshore technical teams and business
* Architected reusable framework to integrate into SAP saving significant cost and reducing timelines
* Developed demand generation and assessment approach for Smart Automation CoE
 
Programme lead, Company 2 – Johannesburg (SA)
January 2017 - December 2017
* Educated and coached more than 100 business participants that delivered 150+ automation solutions leading to significant business benefits and cost savings
* Increased business impact by more than 20% by focusing on outcomes and growing automation opportunities
 
Solution lead and architect, Company 3 – Farnborough (UK), Atyrau (KZ)
January 2016 - December 2016
* Went through a complex architecture and governance process to establish the automation solution based on UiPath with IT and internal controls
* Mapped and optimised process and delivered the automation solution
 
Project and solution lead, Company 4 – Newcastle (UK), San Jose (CR), Manila (PH)
January 2015 - December 2015
* Turned project around after initial process assessment did not identify sufficient benefits
* Successfully delivered savings potential of 100 FTE across individual projects with a combination of process improvement and automation
* Delivered an automation ecosystem based on SAP, BluePrism, ServiceNow, Knime and Spotfire and built capability with the customer to dramatically reduce time spent in finance processes

Solution lead and HR workstream lead, Company 5 – Coventry (UK)
January 2014 - December 2014
* Turned project around given a very demanding customer
* Delivered a Proof of Concept (PoC) to demonstrate automation impact on selected processes
* Business case showed an RoI of 100% with an initial 9-month implementation phase
* Project moved into implementation based on the business case

Solution lead, Company 6 – Budapest (HU), Manila (PH), Bangalore (IN)
January 2013 - December 2013
* Defined a scalable architecture for chosen RPA platform
* Delivered savings of more than 60 FTE and moved into second implementation wave

Project lead, Company 7 – Budapest (HU)
January 2012 - December 2012
* Delivered a Proof of Value (PoV) to demonstrate RPA / data automation impact on selected processes
* Business case demonstrated savings of 25-35% and in some areas, up to 75%, supported by PoV
* Project moved into implementation based on the business case

## Task 1: Deconstruct sentences into their component parts

* Run the text sentence by sentence through Spacy
* Use the dependency graph and part of speech tagging to add context to the above text
  * Dependency visualisation: https://explosion.ai/demos/displacy
* Please note that the dependency parser may not always tag sentences perfectly, so take the below as an approximation


## Ask

* Take a sentence and deconstruct it by parsing the dependency graph

### Example 1 

This is a description of a responsibility. There should be a focus on a verb (what is the candidate required to do).

#### Input

> Understand customer needs and develop high-quality presentations, proposals and software demonstrations that speak to these needs – building a consensus for change on a multi-stakeholder basis

#### Desired output

* Cut the longer sentence into it's component parts

| Output | Suggested rule |
| :--- | :--- |
| Understand customer needs | Look for verb - noun |
| | Verbs 'understand' and 'develop' are connected with a conjunction (and) and hence need to be split into separate lines |
| develop high-quality presentations that speak to these needs | Look for verb - noun and take all other parts of speech |
| develop high-quality proposals that speak to these needs | Nouns are connected with conjunctions (and, or, comma), so replicate the part of the sentence with each noun |
| develop high-quality software demonstrations that speak to these needs | Same as above |
| building a consensus for change on a multi-stakeholder basis | Same as above |

#### Derived output

> Take the above output and reduce it further to remove low-information parts (e.g. adjectives) and cut longer phrases into smaller components parts (looking for nouns and verbs)

| Output | Simplified |
| :--- | :--- |
| Understand customer needs | Understand customer needs |
| develop high-quality presentations that speak to these needs | develop presentations |
| develop high-quality proposals that speak to these needs | develop proposals |
| develop high-quality software demonstrations that speak to these needs | develop software demonstrations |
| building a consensus for change on a multi-stakeholder basis | building consensus for change |

### Example 2

This is a description of a requirements, it will ask for experience with something and may or may not include a verb.

#### Input 

* Experience with a major consulting firm or experience in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies.

#### Desired output

* Cut the longer sentence into it's component parts

| Output | Suggested rule |
| :--- | :--- |
| Experience with a major consulting firm |  |
| Experience in a corporate role | Replicate the above phrase with different noun based on the use of a conjunction |
| delivering strategy projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies | |
| delivering operations projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies | |

#### Derived output

* Take the above output and reduce it further to remove low-information parts (e.g. adjectives) and cut longer phrases into smaller components parts (looking for nouns and verbs)

| Output | Simplified |
| :--- | :--- |
| Experience with a major consulting firm | Experience with consulting firm |
| Experience in a corporate role | Experience in corporate role |
| delivering strategy projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies | delivering strategy projects |
| | business transformation |
| | new operating models |
| | new digital technologies |
| delivering operations projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies | delivering operations projects |

### Example 3

This is a description from a CV and will likely focus on something that was done or had been achieved.

#### Input 

* Went through a complex architecture and governance process to establish the automation solution based on UiPath with IT and internal controls

#### Desired output

* Cut the longer sentence into it's component parts

| Output | Suggested rule |
| :--- | :--- |
| Went through a complex architecture process |  |
| Went through a complex governance process | Replicate the above phrase with different noun based on the use of a conjunction |
| establish the automation solution based on UiPath | Replicate the phase based on different prepositions used |
| establish the automation solution with IT controls | Replicate the phase based on different prepositions used |
| establish the automation solution with internal controls | Replicate the phase based on different prepositions used |

#### Derived output

* Take the above output and reduce it further to remove low-information parts (e.g. adjectives) and cut longer phrases into smaller components parts (looking for nouns and verbs)

| Output | Simplified |
| :--- | :--- |
| Went through a complex architecture process | Went through architecture process |
| Went through a complex governance process | Went through governance process process |
| establish the automation solution based on UiPath | establish automation solution |
| | automation solution based on UiPath |
| establish the automation solution with IT controls | Replicate the phase based on different prepositions used |
| establish the automation solution with internal controls | Replicate the phase based on different prepositions used |

## Task 2: Calculate semantic similarity

Based on the above task you should have a list of component phrases. Please calculate the similarity of each phrase against each other phrase (e.g. use Word2Vec, Spacy or [Google's universal encoder](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb#scrollTo=zwty8Z6mAkdV)). This should leave you with a two dimensional matrix that clusters the similarity of phrases against each other.

Please suggest best approach of comparing similarity of the whole phrase vs. calculating similarity of individual words (with their associated POS) and aggregating to phrase similarity.

## Task 3: Compare and bucket based on semantic similarity

Assuming you compared two different documents in step 2, all sentences should fall into one of three categories:

1. Phrases that are in document 1, but not in document 2
2. Phrases that are in document 2, but not in document 1
3. Phrases that are similar between document 1 and 2, each with a score of similarity (you might have multiple candidates with different similarity for each phrase)

Similarity will likely not be 0, even if the two phrases are very different. Please suggest how to find a cutoff point to bucket similarity into these three buckets.

## Task 4: Align phrases

Lastly, identify within each phrase, which part drives the similarity and what part you would need to replace to make the phases more similar.

* Phrase 1: "Understand customer needs"
* Phrase 2: "Capture business requirements"
  * This will give a fairly high semantic similarity
  
* Question: How can I get from phrase 1 to phrase 2 (assuming that 'customer needs' and 'business requirements' are identified as noun phrases)
  * Alternative 1: "Understand customer needs" > "Capture customer needs" > "Capture business requirements"
  * Alternative 2: "Understand customer needs" > "Understand business requirements" > "Capture business requirements"
 
For more complex phrases, there will be more alternatives on how to get from document 1 to document 2.

Similar to the Levenshtein Distance for spelling error corrections, calculate the steps to get from one phrase to the other. What part of the phrase needs to get replaced and how much would that replacement increase the similarity between these phrases.
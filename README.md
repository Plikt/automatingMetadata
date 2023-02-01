Notion: https://elianna.notion.site/elianna/Automating-Metadata-a8acd0a54e05497dad0faf3ada5f1708

The **goal** of this project is to ignore the current metadata system and start over. We want to know 

- **What metadata is necessary for science?**
    - *Resources*
        - [elicit.](http://elicit.ai)org - This search engine is already scraping metadata through GPT-3 including customization of which data you the user wants. Sometimes it doesn’t return results.
            - I’m not sure if they use GPT for the base metadata (authors, etc) or if they use Semantic Scholar’s API.
        - [https://www.researchobject.org/ro-crate/1.1/](https://www.researchobject.org/ro-crate/1.1/) -> a metadata standard.
            - [https://research.manchester.ac.uk/en/publications/ro-crate-metadata-specification-111](https://research.manchester.ac.uk/en/publications/ro-crate-metadata-specification-111) - the documentation for the project above.
        - Schema.org
        - FAIR data standards
        - Data standards: (
            1. Data origin: experimental, observational, raw or derived, physical collections, models, images, etc.
            2. Data type: integer, Boolean, character, floating point, etc.
            3. Instrument(s) used
            4. Data acquisition details: sensor deployment methods, experimental design, sensor calibration methods, etc.
            5. File type: CSV, mat, xlsx, tiff, HDF, NetCDF, etc.
            6. Data processing methods, software used
            7. Data processing scripts or codes
            8. Dataset parameter list, including
                - Variable names
                - Description of each variable
                - Units
    - *Elaboration*
        - We should explore this at a granular level at the research object (instead of just research node). What is the metadata for code, pdfs, etc?
        - We’re in the exploratory phase -> we want to see what data is in these papers. What can we get out of this?
        - Error in GPT isn’t a super huge problem at the moment -
            - We’re trying to find ways to make things better!
- **How can we eliminate the need for scientists to enter that metadata?**
    - Hypothesis: GPT!
    - Other?
- **********************What else?**********************

**What we have**

- A section for metadata on the node platform.
    - Build out/explore what the Nodes team has discovered through scraping PDFs
    - later on down the road -> integrated into search. But shouldn't think of this as integrating into the nodes platform.
- Emerging Problem statements - (To be edited!)
    - There is no understanding of what metadata is prevalent across all research. There is no standard for that.
        - Connected to ontology.
    - Longer term problem statement -> researchers don't have the knowledge processes/workflows to correctly enter metadata in a standardized format.
        - metadata that is unstandardized and it is difficult to read and use.
        - Difficult to seamlessly tie one piece of research to another (what are the relations between research) ununified scientific record.
        - How might we unify the scientific record w metadata standards that can be accessed by different platforms/gateways so that they can use the research in any way they want.
# Mexican_Political_Party_Tweet_Classifier
**Project by: Jerry Montes**

## Problem Statement

I sought to build a multi-class classification model that, when presented with a tweet from one of the 6 official Twitter accounts associated with Mexican political parties, is capable of determining which party posted it.  **My success criteria involved developing a model that outperformed a baseline model whose accuracy rate was determined by the proportions of each class in the data.**

### Background

Seven national political parties are currently registered in Mexico, which is a federal presidential republic.  From oldest to newest, these are: Partido Acción Nacional (PAN), Partido Revolucionario Institucional (PRI), Partido de la Revolución Democrática (PRD), Partido del Trabajo (PT), Partido Verde Ecologista de México (PV), Movimiento Ciudadano (MC), and Movimiento de Regeneración Nacional (Morena).  A 2021 study found that the majority of Mexicans do not trust their government, whose presidential office was held by the same political party for 71 years straight, whose ex-presidents' alleged wrongdoing would have been investigated following 40% participation in a 2021 referendum, and whose scandals include a governor pleading guilty to embezzling public funds meant for the purchase of chemotherapy for use in state-run hospitals.

When surveyed about what they felt was the primary problem the country was currently facing, the vast majority of respondents reported that Crime was the country's biggest problem.  In fact, three out of every four Mexicans consider their city to be unsafe.  In 2020 around 3,700 women were murdered in Mexico, which is experiencing a femicide crisis.  Corruption was the second most common answer Mexicans gave when asked about what they felt was the primary problem afflicting the country.  Three out of every five Mexicans believe that the majority of police are corrupt, although law enforcement is certainly not the only branch of government that is largely distrusted.  In 2014, public officials submitted false declarations that stated that a Mexico City school's existing walls and floors were being renovated.  In reality its fourth floor, where the school's owner resided, was being expanded without any consideration for whether the building had been built to withstand that additional weight.  This school (which contained the owner's apartment and its marble flooring and bathtub) collapsed during a September 2017 earthquake, killing 19 children and eight adults and serving as an example of how corruption can have deadly consequences.  Given that 44% of the population lives in poverty, it is not surprising that the third most common answer given by Mexicans who were asked about their country's biggest problem involved the economy.  

Mexican political parties certainly have one thing in common: they agree that Mexico needs change.  The proposed path forward differs between parties, along with the specific focus of each party's agenda.  

Six of the seven political parties currently registered with the country's National Electoral Institute (INE) have an official Twitter account.  What follows is a brief description of the six parties with Twitter accounts.
  

## Political party classes:

- To understand where on the spectrum each political party falls, please refer to this 2017 graphic: https://img.buzzfeed.com/buzzfeed-static/static/2017-12/24/21/asset/buzzfeed-prod-fastlane-02/sub-buzz-2594-1514170795-5.png
- "izquierda económica" means **economic left**
- "derecha económica" means **economic right**
- "izquierda política" means **political left**
- "derecha política" means **political right**

- It is worth noting that two of the political parties in the graphic have since lost their registered status after obtaining less than 3% of the vote in 2018 elections. 

**Partido Acción Nacional (National Action Party):** 
This party was registered on March 30th, 1946.  Its current slogan (in English) is "Action or Mexico"

**Partido Revolucionario Institucional (Institutional Revolutionary Party):**
This party was registered on March 30th, 1946.  It held the presidential office for 71 consecutive years, and its current slogan (in English) is "Revolutionaries"

**Partido de la Revolución Democrática (Party of the Democratic Revolution):**
This party was registered on May 26th , 1989.  Its current slogan (in English) is "A new dawn"

**Partido Verde Ecologista de México (Ecological Green Party of Mexico):** 
This party was registered on January 13th, 1993.  Its current slogan (in English) is "Green gets it done"

**Movimiento Ciudadano (Citizens’ Movement):**
This party was registered on June 30th, 1999.  Its current slogan (in English) is "The future is orange"

**Movimiento de Regeneración Nacional (National Regeneration Movement):**
This party was registered on July 9th, 2014.  It currently holds the presidential office, and its current slogan (in English) is "Mexico's hope"


### Approach

I implemented both scikit-learn algorithms and neural networks built using the TensorFlor API to classify text from the tweets obtained.

#### Notebook/Code

|Index|Title|Description|
|---|---|---|
|1|[01_Data_Collection]() | This notebook contains all of the code utilized to pull the 3,200 most recent tweets from the 6 official Twitter accounts associated with Mexican political parties using Twitter's **Twitter API v2**.
|2|[02_Data_Cleaning_& EDA]() | This notebook contains all of the Data Cleaning and Exploratory Data Analysis performed on the data.|
|3|[03_Preprocessing_& Scikit_Learn_Modeling]() | This notebook contains all of the Scikit-learn model development.|
|4|[04_Preprocessing_& Tensorflow_Modeling]() | This notebook contains all of the Tensorflow neural network model development.|

#### Exploratory Data Analysis

During the EDA I performed, I calculated the number of observations of each class in the DataFrame created by concatenating each class' individual DataFrame.  I confirmed that five classes each constituted 16.7% of the data and one class constituted 16.6% of the data.

I then explored each tweet's word count and character length and noted that the tweets with the shortest word count typically consisted only of links that were shared by each user.  I also noted that the tweets with the shortest character length consisted primarily of emojis.  Plotting the word count distribution revealed a normal distribution, and plotting the character length distribution revealed that around a third of the tweets consisted of roughly 140 characters. 

An anaysis of each party's 10 most common unigrams, bigrams, trigrams, 4-grams, and 5-grams using a Spanish-language stop words list revealed that some of the most common words used by the political parties include political party names, their party's slogan, and the current president's name.


__________


### Sources
- https://www.cia.gov/the-world-factbook/field/government-type/
- https://www.theatlantic.com/international/archive/2012/07/party-ruled-mexico-70-years-returns-power/326386/
- https://www.eleconomista.com.mx/politica/7-datos-sobre-la-corrupcion-en-Mexico-segun-Transparencia-Internacional-20171014-0001.html
- https://www.elfinanciero.com.mx/opinion/alejandro-moreno/el-problema-de-la-inseguridad/


### Images

- mexican_flag: https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/1200px-Flag_of_Mexico.svg.png
- usa_flag: :https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/1280px-Flag_of_the_United_States.svg.png
- pri_logo: https://s3.amazonaws.com/s3.timetoast.com/public/uploads/photos/2509205/pri.jpg?1334977688
- gortari: https://yt3.ggpht.com/a/AATXAJwv0AbFNeg17Vwe0sWbxUYTzRS_WpyNY4E70A=s900-c-k-c0xffffffff-no-rj-mo
- duarte: https://mananarm.blob.core.windows.net.optimalcdn.com/images/2015/08/10/javierduarte-focus-0-0-628-524.jpg
- jail_time: https://cdn.laoctava.com/app/uploads/2020/10/8012687659001-scaled.jpg
- travel_advisory: https://travelmaps.state.gov/TSGMap/?extent=-124.207939566,14.44327709,-84.313397286,33.446969624
- femicide: https://www.refinery29.com/images/10192406.png?crop=40:21
- rebsamen: https://www.buzzfeed.com/mx/rafaelcabrera/estas-imagenes-muestran-como-fue-la-ampliacion-del-colegio
- mexico_minimum_wage: https://cdn.vox-cdn.com/thumbor/V1HSR6hyvI0anxP-mw2xeZcKDjE=/0x0:1800x1800/1200x0/filters:focal(0x0:1800x1800):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/15990768/Mexico_minimum_wage.jpg
- prd_logo: http://www.lavozdetamaulipas.mx/wp-content/uploads/2019/02/logo.png
- pan_logo: https://mexico.quadratin.com.mx/www/wp-content/uploads/2014/11/PAN-LOGO-1.jpg
- pv_logo: https://pvemcolima.org.mx/wp-content/uploads/2020/07/Logo-partido-verde-2020.png
- mc_logo: https://www.brandemia.org/sites/default/files/inline/images/logo_movimiento_ciudadano-nuevo.jpg
- morena_logo: https://laextra.mx/wp-content/uploads/2018/11/MORENA-logo.png
- political_spectrum: https://www.buzzfeed.com/mx/yuririaavila/los-politicos-se-tachan-de-izquierda-o-derecha-pero-eso-que
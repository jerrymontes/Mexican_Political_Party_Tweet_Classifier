# Mexican_Political_Party_Tweet_Classifier
**Project by: Jerry Montes**

## Problem Statement

I sought to build a multi-class classification model that, when presented with a tweet from one of the 6 official Twitter accounts associated with Mexican political parties, is capable of determining which party posted it.  **My success criteria involved developing a model that outperformed a baseline model whose accuracy rate was determined by the proportions of each class in the data.**

### Background

Seven national political parties are currently registered in Mexico, which is a federal presidential republic.  From oldest to newest, these are: Partido Acción Nacional (PAN), Partido Revolucionario Institucional (PRI), Partido de la Revolución Democrática (PRD), Partido del Trabajo (PT), Partido Verde Ecologista de México (PV), Movimiento Ciudadano (MC), and Movimiento de Regeneración Nacional (Morena).  A 2021 study found that the majority of Mexicans do not trust their government, whose presidential office was held by the same political party for 71 years straight, whose ex-presidents' alleged wrongdoing would have been investigated following 40% participation in a 2021 referendum, and whose scandals include a governor pleading guilty to embezzling public funds meant for the purchase of chemotherapy for state-run hospitals.

When surveyed about what they felt was the primary problem the country was currently facing, the vast majority of respondents reported that Crime was the country's biggest problem.  In fact, 3 out of every 4 Mexicans consider their city to be unsafe.  In 2020 around 3,700 women were murdered in Mexico, which is experiencing a femicide crisis.  Corruption was the second most common answer Mexicans gave when asked about what they felt was the primary problem afflicting the country.  3 out of every 5 Mexicans believe that the majority of police are corrupt, although law enforcement is certainly not the only branch of government that is largely distrusted.  In 2014, public officials submitted false declarations that stated that a local school's existing walls and floors were being renovated.  In reality its fourth floor, where the school's owner resided, was being expanded without any consideration for whether the building had been built to withstand that additional weight.  This school (which contained the owner's apartment and its marble flooring and bathtub) collapsed during a 2017 earthquake, killing 19 children and eight adults and serving as an example of how corruption can have deadly consequences.



Six of the seven political parties currently recognized by the country's National Electoral Institute have an official Twitter account.
  

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
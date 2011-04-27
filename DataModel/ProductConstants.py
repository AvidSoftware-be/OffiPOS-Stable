from DataModel.ProductGroupConstants import *
from Product import Product

BaronProducts = {
    Frieten: {
        'Frieten_Mini': Product(id=1, price=1.7, name='Mini', group=1),
        'Frieten_Klein': Product(id=2, price=1.9, name='Klein', group=1),
        'Frieten_Midden': Product(id=3, price=2.1, name='Midden', group=1),
        'Frieten_Groot': Product(id=4, price=2.5, name='Groot', group=1),
        'Frieten_Familie': Product(id=5, price=3.7, name='Familie', group=1),
        'Frieten_Kindermenu': Product(id=6, price=5, name='Kindermenu', group=1)},

    Koude_sauzen: {
        'Koude_sauzen_Mayonaise': Product(id=7, price=0.7, name='Mayonaise', group=2),
        'Koude_sauzen_Tartare': Product(id=8, price=0.7, name='Tartare', group=2),
        'Koude_sauzen_Pickles': Product(id=9, price=0.7, name='Pickles', group=2),
        'Koude_sauzen_Pili_Pili': Product(id=10, price=0.7, name='Pili Pili', group=2),
        'Koude_sauzen_Curry': Product(id=11, price=0.7, name='Curry', group=2),
        'Koude_sauzen_Ketchup': Product(id=12, price=0.7, name='Ketchup', group=2),
        'Koude_sauzen_Curry_Ketchup': Product(id=13, price=0.7, name='Curry Ketchup', group=2),
        'Koude_sauzen_Pepersaus': Product(id=14, price=0.7, name='Pepersaus', group=2),
        'Koude_sauzen_Sauce_Riche': Product(id=15, price=0.7, name='Sauce Riche', group=2),
        'Koude_sauzen_Mosterd': Product(id=16, price=0.7, name='Mosterd', group=2),
        'Koude_sauzen_Fritessaus': Product(id=17, price=0.7, name='Fritessaus', group=2),
        'Koude_sauzen_Zigeuner/Provencaal': Product(id=18, price=0.7, name='Zigeuner/Provencaal', group=2),
        'Koude_sauzen_Tartare_Maison': Product(id=19, price=0.7, name='Tartare Maison', group=2),
        'Koude_sauzen_Andalouse': Product(id=20, price=0.7, name='Andalouse', group=2),
        'Koude_sauzen_Americain_Maison': Product(id=21, price=0.7, name='Americain Maison', group=2),
        'Koude_sauzen_Americain': Product(id=22, price=0.7, name='Americain', group=2),
        'Koude_sauzen_Samurai': Product(id=23, price=0.7, name='Samurai', group=2),
        'Koude_sauzen_Ardeense_saus': Product(id=24, price=0.7, name='Ardeense saus', group=2),
        'Koude_sauzen_Bearnaise': Product(id=25, price=0.7, name='Bearnaise', group=2),
        'Koude_sauzen_Brasil': Product(id=26, price=0.7, name='Brasil', group=2),
        'Koude_sauzen_Loempiasaus': Product(id=27, price=0.7, name='Loempiasaus', group=2),
        'Koude_sauzen_Joppiesaus': Product(id=28, price=0.7, name='Joppiesaus', group=2),
        'Koude_sauzen_Cocktail': Product(id=29, price=0.7, name='Cocktail', group=2),
        'Koude_sauzen_Pitta': Product(id=30, price=0.7, name='Pitta', group=2),
        'Koude_sauzen_Chilada_saus': Product(id=31, price=0.7, name='Chilada saus', group=2),
        'Koude_sauzen_Bicky_saus': Product(id=32, price=0.7, name='Bicky saus', group=2),
        'Koude_sauzen_Big_Giant_Hamburgersaus': Product(id=33, price=0.7, name='Big Giant Hamburgersaus', group=2),
        'Koude_sauzen_Portie_Speciaal': Product(id=34, price=1.2, name='Portie Speciaal', group=2)},

    Warme_sauzen: {
        'Warme_sauzen_Stoofvleessaus': Product(id=36, price=1.4, name='Stoofvleessaus', group=3),
        'Warme_sauzen_Tomatensaus': Product(id=37, price=1.4, name='Tomatensaus', group=3),
        'Warme_sauzen_Vol-au-vent_saus': Product(id=38, price=1.4, name='Vol-au-vent saus', group=3),
        'Warme_sauzen_Ghoulash_saus': Product(id=39, price=1.4, name='Ghoulash saus', group=3),
        'Warme_sauzen_Spaghettisaus': Product(id=40, price=1.4, name='Spaghettisaus', group=3)},

    Eigen_bereidingen: {
        'Eigen_bereidingen_Stoofvlees': Product(id=42, price=3.5, name='Stoofvlees', group=4),
        'Eigen_bereidingen_Balletjes_in_tomaat': Product(id=43, price=3.5, name='Balletjes in tomaat',
                                                         group=4),
        'Eigen_bereidingen_Vol-au-vent': Product(id=44, price=3.5, name='Vol-au-vent', group=4),
        'Eigen_bereidingen_Ghoulash': Product(id=45, price=3.5, name='Ghoulash', group=4),
        'Eigen_bereidingen_Spaghetti': Product(id=46, price=4.5, name='Spaghetti', group=4),
        'Eigen_bereidingen_Geraspte_Kaas': Product(id=47, price=0.5, name='Geraspte Kaas', group=4),
        'Eigen_bereidingen_Sate_Klein_150gr': Product(id=48, price=2.5, name='Sate Klein 150gr',
                                                      group=4),
        'Eigen_bereidingen_Sate_Groot_200gr': Product(id=49, price=3, name='Sate Groot 200gr', group=4),
        'Eigen_bereidingen_Kippebout_Sate': Product(id=50, price=2.5, name='Kippebout Sate', group=4),
        'Eigen_bereidingen_Kaaskroket': Product(id=51, price=1.6, name='Kaaskroket', group=4),
        'Eigen_bereidingen_Garnaalkroket': Product(id=52, price=2.7, name='Garnaalkroket', group=4)},

    Hamburgers: {
        'Hamburgers_Bicky': Product(id=54, price=2.6, name='Bicky', group=5),
        'Hamburgers_Bicky_Cheese': Product(id=55, price=2.7, name='Bicky Cheese', group=5),
        'Hamburgers_Bick_Rib': Product(id=56, price=3, name='Bick Rib', group=5),
        'Hamburgers_Bicky_Vegi': Product(id=57, price=2.7, name='Bicky Vegi', group=5),
        'Hamburgers_Bicky_Vegi_Cheese': Product(id=58, price=2.8, name='Bicky Vegi Cheese', group=5),
        'Hamburgers_Bicky_Chicken': Product(id=59, price=3.5, name='Bicky Chicken', group=5),
        'Hamburgers_Chicken_Burger': Product(id=60, price=3.8, name='Chicken Burger', group=5),
        'Hamburgers_Fish_Burger': Product(id=61, price=3.8, name='Fish Burger', group=5),
        'Hamburgers_Giant_Baron_Burger': Product(id=62, price=3.8, name='Giant Baron Burger', group=5),
        'Hamburgers_Red_Baron_Burger': Product(id=63, price=3.8, name='Red Baron Burger', group=5),
        'Hamburgers_Baron_Pepper_Burger': Product(id=64, price=3.8, name='Baron Pepper Burger', group=5),
        'Hamburgers_Cheese_Baron_Burger': Product(id=65, price=3.8, name='Cheese Baron Burger', group=5)},

    Dranken: {
        'Dranken_Blik_33cl': Product(id=66, price=1.5, name='Blik 33cl', group=6),
        'Dranken_Fles_0,5l': Product(id=67, price=2, name='Fles 0,5l', group=6),
        'Dranken_Water_Plat/Bruis': Product(id=68, price=1.1, name='Water Plat/Bruis', group=6),
        'Dranken_Ice_Tea': Product(id=69, price=1.6, name='Ice Tea', group=6),
        'Dranken_Tropico': Product(id=70, price=1.6, name='Tropico', group=6),
        'Dranken_Sinaasappelsap': Product(id=71, price=1.6, name='Sinaasappelsap', group=6),
        'Dranken_Twist&Drink': Product(id=72, price=1.6, name='Twist&Drink', group=6),
        'Dranken_Aquarius': Product(id=73, price=2.5, name='Aquarius', group=6),
        'Dranken_Red_Bull': Product(id=74, price=2.5, name='Red Bull', group=6),
        'Dranken_Jupiler_Blik_33cl': Product(id=75, price=1.6, name='Jupiler Blik 33cl', group=6),
        'Dranken_Jupiler_Blik_50cl': Product(id=76, price=2.3, name='Jupiler Blik 50cl', group=6),
        'Dranken_Hoegaarden': Product(id=77, price=2.7, name='Hoegaarden', group=6),
        'Dranken_Kriek': Product(id=78, price=2.7, name='Kriek', group=6),
        'Dranken_Rode_wijn_25cl': Product(id=79, price=3, name='Rode wijn 25cl', group=6),
        'Dranken_Witte_wijn_25cl': Product(id=80, price=3, name='Witte wijn 25cl', group=6),
        'Dranken_Mojito': Product(id=81, price=0, name='Mojito', group=6)},

    Snacks: {
        'Snacks_Frikandel': Product(id=82, price=1.4, name='Frikandel', group=7),
        'Snacks_Frikandel_Speciaal': Product(id=83, price=2.4, name='Frikandel Speciaal', group=7),
        'Snacks_Bitterbal_5st': Product(id=84, price=1.4, name='Bitterbal 5st', group=7),
        'Snacks_Hamburger': Product(id=85, price=1.4, name='Hamburger', group=7),
        'Snacks_Vleeskroket': Product(id=86, price=1.5, name='Vleeskroket', group=7),
        'Snacks_Boulet': Product(id=87, price=1.6, name='Boulet', group=7),
        'Snacks_Mammoet': Product(id=88, price=1.6, name='Mammoet', group=7),
        'Snacks_Mammoet_+_saus': Product(id=89, price=2.1, name='Mammoet + saus', group=7),
        'Snacks_Pikanto': Product(id=90, price=1.6, name='Pikanto', group=7),
        'Snacks_Ghoulashkroket': Product(id=91, price=1.7, name='Ghoulashkroket', group=7),
        'Snacks_Kipcorn': Product(id=92, price=1.7, name='Kipcorn', group=7),
        'Snacks_Lookworst': Product(id=93, price=1.7, name='Lookworst', group=7),
        'Snacks_Lookworst_Speciaal': Product(id=94, price=2.7, name='Lookworst Speciaal', group=7),
        'Snacks_Ragoezi': Product(id=95, price=1.7, name='Ragoezi', group=7),
        'Snacks_Spicy_Viandelle': Product(id=96, price=1.7, name='Spicy Viandelle', group=7),
        'Snacks_Viandel': Product(id=97, price=1.7, name='Viandel', group=7),
        'Snacks_Mexicano': Product(id=98, price=2, name='Mexicano', group=7),
        'Snacks_Zigeunerstick': Product(id=99, price=2, name='Zigeunerstick', group=7),
        'Snacks_Fishburger': Product(id=100, price=2.1, name='Fishburger', group=7),
        'Snacks_Boulet_Maison': Product(id=101, price=2.2, name='Boulet Maison', group=7),
        'Snacks_Ribster': Product(id=102, price=2.3, name='Ribster', group=7),
        'Snacks_Kipschnitsel': Product(id=103, price=2.5, name='Kipschnitsel', group=7),
        'Snacks_Mini_Loempia_6st': Product(id=104, price=2.5, name='Mini Loempia 6st', group=7),
        'Snacks_Taco': Product(id=105, price=2.5, name='Taco', group=7),
        'Snacks_Vuurvreter': Product(id=106, price=2.5, name='Vuurvreter', group=7),
        'Snacks_Ardeense_sate': Product(id=107, price=2.6, name='Ardeense sate', group=7),
        'Snacks_Loempia_Kip': Product(id=108, price=2.6, name='Loempia Kip', group=7),
        'Snacks_Chixfingers': Product(id=109, price=2.7, name='Chixfingers', group=7),
        'Snacks_Crizly': Product(id=110, price=2.7, name='Crizly', group=7),
        'Snacks_Fishstick': Product(id=111, price=2.7, name='Fishstick', group=7),
        'Snacks_Ivo': Product(id=112, price=2.7, name='Ivo', group=7),
        'Snacks_Kippets': Product(id=113, price=2.7, name='Kippets', group=7),
        'Snacks_Sito_Gold': Product(id=114, price=2.7, name='Sito Gold', group=7),
        'Snacks_Mitraillette': Product(id=115, price=3.3, name='Mitraillette', group=7)}
}
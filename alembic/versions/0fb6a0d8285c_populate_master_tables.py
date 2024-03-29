"""Populate master tables

Revision ID: 0fb6a0d8285c
Revises: a3dbfd8cdc6b
Create Date: 2024-02-29 16:20:05.998758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fb6a0d8285c'
down_revision: Union[str, None] = 'a3dbfd8cdc6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO province (name) VALUES 
    ('Koshi'), 
    ('Madhesh'), 
    ('Bagmati'), 
    ('Gandaki'), 
    ('Lumbini'), 
    ('Karnali'), 
    ('Sudurpaschim');
    """)
    
    op.execute("""
    INSERT INTO district (name, province_id) VALUES 
    ('Taplejung', 1), 
    ('Sankhuwasabha', 1), 
    ('Solukhumbu', 1), 
    ('Okhaldhunga', 1), 
    ('Khotang', 1), 
    ('Bhojpur', 1), 
    ('Dhankuta', 1), 
    ('Terhathum', 1), 
    ('Panchthar', 1), 
    ('Ilam', 1), 
    ('Jhapa', 1), 
    ('Morang', 1), 
    ('Sunsari', 1), 
    ('Udayapur', 1), 
    ('Saptari', 2), 
    ('Siraha', 2), 
    ('Dhanusa', 2), 
    ('Mahottari', 2), 
    ('Sarlahi', 2), 
    ('Rautahat', 2), 
    ('Bara', 2), 
    ('Parsa', 2), 
    ('Dolakha', 3), 
    ('Sindhupalchok', 3), 
    ('Rasuwa', 3), 
    ('Dhading', 3), 
    ('Nuwakot', 3), 
    ('Kathmandu', 3), 
    ('Bhaktapur', 3), 
    ('Lalitpur', 3), 
    ('Kavrepalanchok', 3), 
    ('Ramechhap', 3), 
    ('Sindhuli', 3), 
    ('Makwanpur', 3), 
    ('Chitawan', 3), 
    ('Gorkha', 4), 
    ('Manang', 4), 
    ('Mustang', 4), 
    ('Myagdi', 4), 
    ('Kaski', 4), 
    ('Lamjung', 4), 
    ('Tanahu', 4), 
    ('Nawalparasi (Bardaghat Susta East)', 4), 
    ('Syangja', 4), 
    ('Parbat', 4), 
    ('Baglung', 4), 
    ('Rukum (East)', 5), 
    ('Rolpa', 5), 
    ('Pyuthan', 5), 
    ('Gulmi', 5), 
    ('Arghakhanchi', 5), 
    ('Palpa', 5), 
    ('Nawalparasi (Bardaghat Susta West)', 5), 
    ('Rupandehi', 5), 
    ('Kapilbastu', 5), 
    ('Dang', 5), 
    ('Banke', 5), 
    ('Bardiya', 5), 
    ('Dolpa', 6), 
    ('Mugu', 6), 
    ('Humla', 6), 
    ('Jumla', 6), 
    ('Kalikot', 6), 
    ('Dailekh', 6), 
    ('Jajarkot', 6), 
    ('Rukum (West)', 6), 
    ('Salyan', 6), 
    ('Surkhet', 6), 
    ('Bajura', 7), 
    ('Bajhang', 7), 
    ('Darchula', 7), 
    ('Baitadi', 7), 
    ('Dadeldhura', 7), 
    ('Doti', 7), 
    ('Achham', 7), 
    ('Kailali', 7), 
    ('Kanchanpur', 7);
    """)
    
    op.execute("""
    INSERT INTO municipality (name, num_of_ward, district_id) VALUES 
    ('Phaktanlung Gaunpalika', 7, 1), 
    ('Mikwakhola Gaunpalika', 5, 1), 
    ('Meringden Gaunpalika', 6, 1), 
    ('Maiwakhola Gaunpalika', 6, 1), 
    ('Aatharai Tribeni Gaunpalika', 5, 1), 
    ('Phungling Municipality', 11, 1), 
    ('Pathivara Yangwarak Gaunpalika', 6, 1), 
    ('Sirijanga Gaunpalika', 8, 1), 
    ('Sidingba Gaunpalika', 7, 1), 
    ('Bhotkhola Gaunpalika', 5, 2), 
    ('Makalu Gaunpalika', 6, 2), 
    ('Silichong Gaunpalika', 5, 2), 
    ('Chichila Gaunpalika', 5, 2), 
    ('Sabhapokhari Gaunpalika', 6, 2), 
    ('Khandabari Municipality', 11, 2), 
    ('Panchakhapan Municipality', 9, 2), 
    ('Chainapur Municipality', 11, 2), 
    ('Madi Municipality', 9, 2), 
    ('Dharmadevi Municipality', 9, 2), 
    ('Khumbu Pasanglhamu Gaunpalika', 5, 3), 
    ('Mahakulung Gaunpalika', 5, 3), 
    ('Sotang Gaunpalika', 5, 3), 
    ('Mapya Dudhkoshi Gaunpalika', 7, 3), 
    ('Thulung Dudhkoshi Gaunpalika', 9, 3), 
    ('Necha Salyan Gaunpalika', 5, 3), 
    ('Solu Dhudhakunda Municipality', 11, 3), 
    ('Likhu Pike Gaunpalika', 5, 3), 
    ('Chishankhu Gadhi Gaunpalika', 8, 4), 
    ('Siddhicharan Municipality', 12, 4), 
    ('Molung Gaunpalika', 8, 4), 
    ('Khiji Demba Gaunpalika', 9, 4), 
    ('Likhu Gaunpalika', 9, 4), 
    ('Champadevi Gaunpalika', 10, 4), 
    ('Sunkoshi Gaunpalika', 10, 4), 
    ('Manebhanjyang Gaunpalika', 9, 4), 
    ('Kepilasgadhi Gaunpalika', 7, 5), 
    ('Aiselukharka Gaunpalika', 7, 5), 
    ('Rawa Besi Gaunpalika', 6, 5), 
    ('Halesi Tuwachung Municipality', 11, 5), 
    ('Diktel Rupakot Majhuwagadhi Municipality', 15, 5), 
    ('Sakela Gaunpalika', 5, 5), 
    ('Diprung Chuichumma Gaunpalika', 7, 5), 
    ('Khotehang Gaunpalika', 9, 5), 
    ('Jante Dhunga Gaunpalika', 6, 5), 
    ('Baraha Pokhari Gaunpalika', 6, 5), 
    ('Shadananda Municipality', 14, 6), 
    ('Salpa Silichho Gaunpalika', 6, 6), 
    ('Temkemaiyum Gaunpalika', 9, 6), 
    ('Bhojpur Municipality', 12, 6), 
    ('Arun Gaunpalika', 7, 6), 
    ('Pauwa Dunma Gaunpalika', 6, 6), 
    ('Ramprasad Rai Gaunpalika', 8, 6), 
    ('Hatuwagadhi Gaunpalika', 9, 6), 
    ('Aamchowk Gaunpalika', 10, 6), 
    ('Mahalaxmi Municipality', 9, 7), 
    ('Pakhribas Municipality', 10, 7), 
    ('Chhathar Jorpati Gaunpalika', 6, 7), 
    ('Dhankuta Municipality', 10, 7), 
    ('Shahidbhumi Gaunpalika', 7, 7), 
    ('Sangurigadhi Gaunpalika', 10, 7), 
    ('Chaubise Gaunpalika', 8, 7), 
    ('Aatharai Gaunpalika', 7, 8), 
    ('Phedap Gaunpalika', 5, 8), 
    ('Menchhayayem Gaunpalika', 6, 8), 
    ('Myanglung Municipality', 10, 8), 
    ('Laligurans Municipality', 9, 8), 
    ('Chhathar Gaunpalika', 6, 8), 
    ('Yangbarak Gaunpalika', 6, 9), 
    ('Hilihan Gaunpalika', 7, 9), 
    ('Falelung Gaunpalika', 8, 9), 
    ('Phidim Municipality', 14, 9), 
    ('Falgunanda Gaunpalika', 7, 9), 
    ('Kummayak Gaunpalika', 5, 9), 
    ('Tumbewa Gaunpalika', 5, 9), 
    ('Miklajung Gaunpalika', 8, 9), 
    ('Mai Jogmai Gaunpalika', 6, 10), 
    ('Sandakpur Gaunpalika', 5, 10), 
    ('Illam Municipality', 12, 10), 
    ('Deumai Municipality', 9, 10), 
    ('Fakfokathum Gaunpalika', 7, 10), 
    ('Mangsebung Gaunpalika', 6, 10), 
    ('Chulachuli Gaunpalika', 6, 10), 
    ('Mai Municipality', 10, 10), 
    ('Suryodaya Municipality', 14, 10), 
    ('Rong Gaunpalika', 6, 10), 
    ('Mechinagar Municipality', 15, 11), 
    ('Buddhashanti Gaunpalika', 7, 11), 
    ('Arjundhara Municipality', 11, 11), 
    ('Kankai Municipality', 9, 11), 
    ('Shivasatakshi Municipality', 11, 11), 
    ('Kamal Gaunpalika', 7, 11), 
    ('Damak Municipality', 10, 11), 
    ('Gauradaha Municipality', 9, 11), 
    ('Gauriganj Gaunpalika', 6, 11), 
    ('Jhapa Gaunpalika', 7, 11), 
    ('Barhadashi Gaunpalika', 7, 11), 
    ('Birtamod Municipality', 10, 11), 
    ('Haldibari Gaunpalika', 5, 11), 
    ('Bhadrapur Municipality', 10, 11), 
    ('Kachanakawal Gaunpalika', 7, 11), 
    ('Miklajung Gaunpalika', 9, 12), 
    ('Letang Municipality', 9, 12), 
    ('Kerabari Gaunpalika', 10, 12), 
    ('Sundarharaicha Municipality', 12, 12), 
    ('Belbari Municipality', 11, 12), 
    ('Kanepokhari Gaunpalika', 7, 12), 
    ('Pathari Shanishchare Municipality', 10, 12), 
    ('Urlabari Municipality', 9, 12), 
    ('Ratuwamai Municipality', 10, 12), 
    ('Sunwarshi Municipality', 9, 12), 
    ('Rangeli Municipality', 9, 12), 
    ('Gramthan Gaunpalika', 7, 12), 
    ('Budhiganga Gaunpalika', 7, 12), 
    ('Biratnagar Metropolitian City', 19, 12), 
    ('Katahari Gaunpalika', 7, 12), 
    ('Dhanapalthan Gaunpalika', 7, 12), 
    ('Jahada Gaunpalika', 7, 12), 
    ('Dharan Sub-Metropolitian City', 20, 13), 
    ('Barahachhetra Municipality', 11, 13), 
    ('Koshi Gaunpalika', 8, 13), 
    ('Bhokraha Narsingh Gaunpalika', 8, 13), 
    ('Ramdhuni Municipality', 9, 13), 
    ('Itahari Sub-Metropolitian City', 20, 13), 
    ('Duhabi Municipality', 12, 13), 
    ('Gadhi Gaunpalika', 6, 13), 
    ('Inaruwa Municipality', 10, 13), 
    ('Harinagar Gaunpalika', 7, 13), 
    ('Dewangunj Gaunpalika', 7, 13), 
    ('Barju Gaunpalika', 6, 13), 
    ('Belaka Municipality', 9, 14), 
    ('Chaudandigadhi Municipality', 10, 14), 
    ('Triyuga Municipality', 16, 14), 
    ('Rautamai Gaunpalika', 8, 14), 
    ('Limchunbung Gaunpalika', 5, 14), 
    ('Tapli Gaunpalika', 5, 14), 
    ('Katari Municipality', 14, 14), 
    ('Udayapurgadhi Gaunpalika', 8, 14), 
    ('Saptakoshi Municipality', 11, 15), 
    ('Kanchanrup Municipality', 12, 15), 
    ('Agnisair Krishna Sabaran Gaunpalika', 6, 15), 
    ('Rupani Gaunpalika', 6, 15), 
    ('Shambhunath Municipality', 12, 15), 
    ('Khadak Municipality', 11, 15), 
    ('Surunga Municipality', 11, 15), 
    ('Balan-Bihul Gaunpalika', 6, 15), 
    ('Bode Barsain Municipality', 10, 15), 
    ('Dakneshwori Municipality', 10, 15), 
    ('Rajgadh Gaunpalika', 6, 15), 
    ('Bishnupur Gaunpalika', 7, 15), 
    ('Rajbiraj Municipality', 16, 15), 
    ('Mahadewa Gaunpalika', 6, 15), 
    ('Tirahut Gaunpalika', 5, 15), 
    ('Hanumannagar Kankalini Municipality', 14, 15), 
    ('Tilathi Koiladi Gaunpalika', 8, 15), 
    ('Chhinnamasta Gaunpalika', 7, 15), 
    ('Lahan Municipality', 24, 16), 
    ('Dhangadhimai Municipality', 14, 16), 
    ('Golbazar Municipality', 13, 16), 
    ('Mirchaiya Municipality', 12, 16), 
    ('Karjanha Municipality', 11, 16), 
    ('Kalyanpur Municipality', 12, 16), 
    ('Naraha Gaunpalika', 5, 16), 
    ('Bishnupur Gaunpalika', 5, 16), 
    ('Arnama Gaunpalika', 5, 16), 
    ('Sukhipur Municipality', 10, 16), 
    ('Laxmipur Patari Gaunpalika', 6, 16), 
    ('Sakhuwa Nankarkatti Gaunpalika', 5, 16), 
    ('Bhagawanpur Gaunpalika', 5, 16), 
    ('Nawarajpur Gaunpalika', 5, 16), 
    ('Bariyarpatti Gaunpalika', 5, 16), 
    ('Aurahi Gaunpalika', 5, 16), 
    ('Siraha Municipality', 22, 16), 
    ('Ganeshman Charnath Municipality', 11, 17), 
    ('Dhanushadham Municipality', 9, 17), 
    ('Mithila Municipality', 11, 17), 
    ('Bateshwor Gaunpalika', 5, 17), 
    ('Chhireshwornath Municipality', 10, 17), 
    ('Laxminiya Gaunpalika', 7, 17), 
    ('Mithila Bihari Municipality', 10, 17), 
    ('Hansapur Municipality', 9, 17), 
    ('Sabaila Municipality', 13, 17), 
    ('Shahidnagar Municipality', 9, 17), 
    ('Kamala Municipality', 9, 17), 
    ('Janak Nandini Gaunpalika', 6, 17), 
    ('Bideha Municipality', 9, 17), 
    ('Aurahi Gaunpalika', 6, 17), 
    ('Janakpurdham Sub-Metropolitian City', 25, 17), 
    ('Dhanauji Gaunpalika', 5, 17), 
    ('Nagarain Municipality', 9, 17), 
    ('Mukhiyapatti Musaharmiya Gaunpalika', 6, 17), 
    ('Bardibas Municipality', 14, 18), 
    ('Gaushala Municipality', 12, 18), 
    ('Sonama Gaunpalika', 8, 18), 
    ('Aurahi Municipality', 9, 18), 
    ('Bhangaha Municipality', 9, 18), 
    ('Loharpatti Municipality', 9, 18), 
    ('Balawa Municipality', 11, 18), 
    ('Ram Gopalpur Municipality', 9, 18), 
    ('Samsi Gaunpalika', 7, 18), 
    ('Manara Shisawa Municipality', 10, 18), 
    ('Ekadara Gaunpalika', 6, 18), 
    ('Mahottari Gaunpalika', 6, 18), 
    ('Pipara Gaunpalika', 7, 18), 
    ('Matihani Municipality', 9, 18), 
    ('Jaleshwor Municipality', 12, 18), 
    ('Lalbandi Municipality', 17, 19), 
    ('Hariwan Municipality', 11, 19), 
    ('Bagmati Municipality', 12, 19), 
    ('Barahathawa Municipality', 18, 19), 
    ('Haripur Municipality', 9, 19), 
    ('Ishworpur Municipality', 15, 19), 
    ('Haripurwa Municipality', 9, 19), 
    ('Parsa Gaunpalika', 6, 19), 
    ('Brahmapuri Gaunpalika', 7, 19), 
    ('Chandranagar Gaunpalika', 7, 19), 
    ('Kabilashi Municipality', 10, 19), 
    ('Chakraghatta Gaunpalika', 9, 19), 
    ('Basbariya Gaunpalika', 6, 19), 
    ('Dhanakaul Gaunpalika', 7, 19), 
    ('Ramnagar Gaunpalika', 7, 19), 
    ('Balara Municipality', 11, 19), 
    ('Godaita Municipality', 12, 19), 
    ('Bishnu Gaunpalika', 8, 19), 
    ('Kaudena Gaunpalika', 7, 19), 
    ('Malangawa Municipality', 12, 19), 
    ('Chandrapur Municipality', 10, 20), 
    ('Gujara Municipality', 9, 20), 
    ('Phatuwa Bijayapur Municipality', 11, 20), 
    ('Katahariya Municipality', 9, 20), 
    ('Brindaban Municipality', 9, 20), 
    ('Gadhimai Municipality', 9, 20), 
    ('Madhav Narayan Municipality', 9, 20), 
    ('Garuda Municipality', 9, 20), 
    ('Dewahi Gonahi Municipality', 9, 20), 
    ('Maulapur Municipality', 9, 20), 
    ('Boudhimai Municipality', 9, 20), 
    ('Paroha Municipality', 9, 20), 
    ('Rajpur Municipality', 9, 20), 
    ('Yamunamai Gaunpalika', 5, 20), 
    ('Durga Bhagawati Gaunpalika', 5, 20), 
    ('Rajdevi Municipality', 9, 20), 
    ('Gaur Municipality', 9, 20), 
    ('Ishanath Municipality', 9, 20), 
    ('Nijagadh Municipality', 13, 21), 
    ('Kolhabi Municipality', 11, 21), 
    ('Jitpur Simara Sub-Metropolitian City', 24, 21), 
    ('Parawanipur Gaunpalika', 5, 21), 
    ('Prasauni Gaunpalika', 7, 21), 
    ('Bishrampur Gaunpalika', 5, 21), 
    ('Pheta Gaunpalika', 7, 21), 
    ('Kalaiya Sub-Metropolitian City', 27, 21), 
    ('Karaiyamai Gaunpalika', 8, 21), 
    ('Baragadhi Gaunpalika', 6, 21), 
    ('Aadarsha Kotwal Gaunpalika', 8, 21), 
    ('Simroungadh Municipality', 11, 21), 
    ('Pacharauta Municipality', 9, 21), 
    ('Mahagadhimai Municipality', 11, 21), 
    ('Devtal Gaunpalika', 7, 21), 
    ('Subarna Gaunpalika', 8, 21), 
    ('Thori Gaunpalika', 5, 22), 
    ('Jirabhawani Gaunpalika', 5, 22), 
    ('Jagarnathpur Gaunpalika', 6, 22), 
    ('Paterwa Sugauli Gaunpalika', 5, 22), 
    ('Sakhuwa Prasauni Gaunpalika', 6, 22), 
    ('Parsagadhi Municipality', 9, 22), 
    ('Birgunj Metropolitian City', 32, 22), 
    ('Bahudarmai Municipality', 9, 22), 
    ('Pokhariya Municipality', 10, 22), 
    ('Kalikamai Gaunpalika', 5, 22), 
    ('Dhobini Gaunpalika', 5, 22), 
    ('Chhipaharmai Gaunpalika', 5, 22), 
    ('Pakaha Mainpur Gaunpalika', 5, 22), 
    ('Bindabasini Gaunpalika', 5, 22), 
    ('Gaurishankar Gaunpalika', 9, 23), 
    ('Bigu Gaunpalika', 8, 23), 
    ('Kalinchowk Gaunpalika', 9, 23), 
    ('Baiteshwor Gaunpalika', 8, 23), 
    ('Jiri Municipality', 9, 23), 
    ('Tamakoshi Gaunpalika', 7, 23), 
    ('Melung Gaunpalika', 7, 23), 
    ('Shailung Gaunpalika', 8, 23), 
    ('Bhimeshwor Municipality', 9, 23), 
    ('Bhotekoshi Gaunpalika', 5, 24), 
    ('Jugal Gaunpalika', 7, 24), 
    ('Panchpokhari Thangpal Gaunpalika', 8, 24), 
    ('Helambu Gaunpalika', 7, 24), 
    ('Melanchi Municipality', 13, 24), 
    ('Indrawoti Gaunpalika', 12, 24), 
    ('Choutara Sangachowkgadhi Municipality', 14, 24), 
    ('Balephi Gaunpalika', 8, 24), 
    ('Bahrabise Municipality', 9, 24), 
    ('Tripurasundari Gaunpalika', 6, 24), 
    ('Lisankhu Pakhar Gaunpalika', 7, 24), 
    ('Sunkoshi Gaunpalika', 7, 24), 
    ('Gosaikunda Gaunpalika', 6, 25), 
    ('Aamachhodingmo Gaunpalika', 5, 25), 
    ('Uttargaya Gaunpalika', 5, 25), 
    ('Kalika Gaunpalika', 5, 25), 
    ('Naukunda Gaunpalika', 6, 25), 
    ('Rubi Valley Gaunpalika', 6, 26), 
    ('Khaniyabas Gaunpalika', 5, 26), 
    ('Ganga Jamuna Gaunpalika', 7, 26), 
    ('Tripurasundari Gaunpalika', 7, 26), 
    ('Netrawati Dabjong Gaunpalika', 5, 26), 
    ('Nilkhantha Municipality', 14, 26), 
    ('Jwalamukhi Gaunpalika', 7, 26), 
    ('Siddhalek Gaunpalika', 7, 26), 
    ('Benighat Rorang Gaunpalika', 10, 26), 
    ('Gajuri Gaunpalika', 8, 26), 
    ('Galchhi Gaunpalika', 8, 26), 
    ('Thakre Gaunpalika', 11, 26), 
    ('Dhunibenshi Municipality', 9, 26), 
    ('Dupcheshwor Gaunpalika', 7, 27), 
    ('Tadi Gaunpalika', 6, 27), 
    ('Suryagadhi Gaunpalika', 5, 27), 
    ('Bidur Municipality', 13, 27), 
    ('Kispang Gaunpalika', 5, 27), 
    ('Myagang Gaunpalika', 6, 27), 
    ('Tarakeshwor Gaunpalika', 6, 27), 
    ('Belkotgadhi Municipality', 13, 27), 
    ('Likhu Gaunpalika', 6, 27), 
    ('Panchakanya Gaunpalika', 5, 27), 
    ('Shivapuri Gaunpalika', 8, 27), 
    ('Kakani Gaunpalika', 8, 27), 
    ('Shankharapur Municipality', 9, 28), 
    ('Kageshwori Manahara Municipality', 9, 28), 
    ('Gokarneshwor Municipality', 9, 28), 
    ('Budhanilkhantha Municipality', 13, 28), 
    ('Tokha Municipality', 11, 28), 
    ('Tarakeshwor Municipality', 11, 28), 
    ('Nagarjun Municipality', 10, 28), 
    ('Kathmandu Metropolitian City', 32, 28), 
    ('Kirtipur Municipality', 10, 28), 
    ('Chandragiri Municipality', 15, 28), 
    ('Dakshinkali Municipality', 9, 28), 
    ('Changunarayan Municipality', 9, 29), 
    ('Bhaktapur Municipality', 10, 29), 
    ('Madhyapur Thimi Municipality', 9, 29), 
    ('Suryabinayak Municipality', 10, 29), 
    ('Mahalaxmi Municipality', 10, 30), 
    ('Lalitpur Metropolitian City', 29, 30), 
    ('Godawari Municipality', 14, 30), 
    ('Konjyosom Gaunpalika', 5, 30), 
    ('Mahankal Gaunpalika', 6, 30), 
    ('Bagmati Gaunpalika', 7, 30), 
    ('Chauri Deurali Gaunpalika', 9, 31), 
    ('Bhumlu Gaunpalika', 10, 31), 
    ('Mandan Deupur Municipality', 12, 31), 
    ('Banepa Municipality', 14, 31), 
    ('Dhulikhel Municipality', 12, 31), 
    ('Panchkhal Municipality', 13, 31), 
    ('Temal Gaunpalika', 9, 31), 
    ('Namobuddha Municipality', 11, 31), 
    ('Panauti Municipality', 12, 31), 
    ('Bethanchowk Gaunpalika', 6, 31), 
    ('Roshi Gaunpalika', 12, 31), 
    ('Mahabharat Gaunpalika', 8, 31), 
    ('Khanikhola Gaunpalika', 7, 31), 
    ('Umakunda Gaunpalika', 7, 32), 
    ('Gokulganga Gaunpalika', 6, 32), 
    ('Likhu Tamakoshi Gaunpalika', 7, 32), 
    ('Ramechhap Municipality', 9, 32), 
    ('Manthali Municipality', 14, 32), 
    ('Khandadevi Gaunpalika', 9, 32), 
    ('Doramba Gaunpalika', 7, 32), 
    ('Sunapati Gaunpalika', 5, 32), 
    ('Dudhouli Municipality', 14, 33), 
    ('Phikkal Gaunpalika', 6, 33), 
    ('Tinpatan Gaunpalika', 11, 33), 
    ('Golanjor Gaunpalika', 7, 33), 
    ('Kamalamai Municipality', 14, 33), 
    ('Sunkoshi Gaunpalika', 7, 33), 
    ('Ghyanglekha Gaunpalika', 5, 33), 
    ('Marin Gaunpalika', 7, 33), 
    ('Hariharpurgaghi Gaunpalika', 8, 33), 
    ('Indrasarowar Gaunpalika', 5, 34), 
    ('Thaha Municipality', 12, 34), 
    ('Kailash Gaunpalika', 10, 34), 
    ('Raksirang Gaunpalika', 9, 34), 
    ('Manahari Gaunpalika', 9, 34), 
    ('Hetauda Sub-Metropolitian City', 19, 34), 
    ('Bhimphedi Gaunpalika', 9, 34), 
    ('Makawanpurgadhi Gaunpalika', 8, 34), 
    ('Bakaiya Gaunpalika', 12, 34), 
    ('Bagmati Gaunpalika', 9, 34), 
    ('Rapti Municipality', 13, 35), 
    ('Kalika Municipality', 11, 35), 
    ('Ichchha Kamana Gaunpalika', 7, 35), 
    ('Bharatpur Metropolitian City', 29, 35), 
    ('Ratnanagar Municipality', 16, 35), 
    ('Khairahani Municipality', 13, 35), 
    ('Madi Municipality', 9, 35), 
    ('Chumanubri Gaunpalika', 7, 36), 
    ('Ajirkot Gaunpalika', 5, 36), 
    ('Barpak Sulikot Gaunpalika', 8, 36), 
    ('Dharche Gaunpalika', 7, 36), 
    ('Aarughat Gaunpalika', 10, 36), 
    ('Bhimsenthapa Gaunpalika', 8, 36), 
    ('Siranchowk Gaunpalika', 8, 36), 
    ('Palungtar Municipality', 10, 36), 
    ('Gorkha Municipality', 14, 36), 
    ('Shahid Lakhan Gaunpalika', 9, 36), 
    ('Gandaki Gaunpalika', 8, 36), 
    ('Narpa Bhumi Gaunpalika', 5, 37), 
    ('Manang Ngisyang Gaunpalika', 9, 37), 
    ('Chame Gaunpalika', 5, 37), 
    ('Nason Gaunpalika', 9, 37), 
    ('Lo Ghekar Damodarkunda Gaunpalika', 5, 38), 
    ('Gharpajhong Gaunpalika', 5, 38), 
    ('Varagung Muktichhetra Gaunpalika', 5, 38), 
    ('Lomanthang Gaunpalika', 5, 38), 
    ('Thasang Gaunpalika', 5, 38), 
    ('Annapurna Gaunpalika', 8, 39), 
    ('Raghuganga Gaunpalika', 8, 39), 
    ('Dhawalagiri Gaunpalika', 7, 39), 
    ('Malika Gaunpalika', 7, 39), 
    ('Mangala Gaunpalika', 5, 39), 
    ('Beni Municipality', 10, 39), 
    ('Madi Gaunpalika', 12, 40), 
    ('Machhapuchchhre Gaunpalika', 9, 40), 
    ('Annapurna Gaunpalika', 11, 40), 
    ('Pokhara Metropolitian City', 33, 40), 
    ('Rupa Gaunpalika', 7, 40), 
    ('Dordi Gaunpalika', 9, 41), 
    ('Marshyangdi Gaunpalika', 9, 41), 
    ('Kwhola Sothar Gaunpalika', 9, 41), 
    ('Madhya Nepal Municipality', 10, 41), 
    ('Bensishahar Municipality', 11, 41), 
    ('Sundarbazar Municipality', 11, 41), 
    ('Rainas Municipality', 10, 41), 
    ('Dudhapokhari Gaunpalika', 6, 41), 
    ('Bhanu Municipality', 13, 42), 
    ('Byas Municipality', 14, 42), 
    ('Myagde Gaunpalika', 7, 42), 
    ('Shuklagandaki Municipality', 12, 42), 
    ('Bhimad Municipality', 9, 42), 
    ('Ghiring Gaunpalika', 5, 42), 
    ('Rhishing Gaunpalika', 8, 42), 
    ('Devghat Gaunpalika', 5, 42), 
    ('Bandipur Gaunpalika', 6, 42), 
    ('Aanbu Khaireni Gaunpalika', 6, 42), 
    ('Gaidakot Municipality', 18, 43), 
    ('Bulingtar Gaunpalika', 6, 43), 
    ('Baudikali Gaunpalika', 6, 43), 
    ('Hupsekot Gaunpalika', 6, 43), 
    ('Devchuli Municipality', 17, 43), 
    ('Kawasoti Municipality', 17, 43), 
    ('Madhya Bindu Municipality', 15, 43), 
    ('Binayi Tribeni Gaunpalika', 7, 43), 
    ('Putalibazar Municipality', 14, 44), 
    ('Phedikhola Gaunpalika', 5, 44), 
    ('Aandhikhola Gaunpalika', 6, 44), 
    ('Arjun Choupari Gaunpalika', 6, 44), 
    ('Bhirkot Municipality', 9, 44), 
    ('Biruwa Gaunpalika', 8, 44), 
    ('Harinas Gaunpalika', 7, 44), 
    ('Chapakot Municipality', 10, 44), 
    ('Walling Municipality', 14, 44), 
    ('Galyang Municipality', 11, 44), 
    ('Kaligandaki Gaunpalika', 7, 44), 
    ('Modi Gaunpalika', 8, 45), 
    ('Jaljala Gaunpalika', 9, 45), 
    ('Kushma Municipality', 14, 45), 
    ('Phalebas Municipality', 11, 45), 
    ('Mahashila Gaunpalika', 6, 45), 
    ('Bihadi Gaunpalika', 6, 45), 
    ('Paiyu Gaunpalika', 7, 45), 
    ('Baglung Municipality', 14, 46), 
    ('Kathekhola Gaunpalika', 8, 46), 
    ('Tarakhola Gaunpalika', 5, 46), 
    ('Tamankhola Gaunpalika', 6, 46), 
    ('Dhorpatan Municipality', 9, 46), 
    ('Nisikhola Gaunpalika', 7, 46), 
    ('Badigad Gaunpalika', 10, 46), 
    ('Galkot Municipality', 11, 46), 
    ('Bareng Gaunpalika', 5, 46), 
    ('Jaimuni Municipality', 10, 46), 
    ('Putha Uttanganga Gaunpalika', 14, 47), 
    ('Sisne Gaunpalika', 8, 47), 
    ('Bhoome Gaunpalika', 9, 47), 
    ('Sunchhahari Gaunpalika', 7, 48), 
    ('Thawang Gaunpalika', 5, 48), 
    ('Pariwartan Gaunpalika', 6, 48), 
    ('Gangadev Gaunpalika', 7, 48), 
    ('Madi Gaunpalika', 6, 48), 
    ('Tribeni Gaunpalika', 7, 48), 
    ('Rolpa Municipality', 10, 48), 
    ('Runtigadhi Gaunpalika', 9, 48), 
    ('Sunil Smriti Gaunpalika', 8, 48), 
    ('Lungri Gaunpalika', 7, 48), 
    ('Gaumukhi Gaunpalika', 7, 49), 
    ('Naubahini Gaunpalika', 8, 49), 
    ('Jhimaruk Gaunpalika', 8, 49), 
    ('Pyuthan Municipality', 10, 49), 
    ('Sworgadwari Municipality', 9, 49), 
    ('Mandavi Gaunpalika', 5, 49), 
    ('Mallarani Gaunpalika', 5, 49), 
    ('Aairawati Gaunpalika', 6, 49), 
    ('Sarumarani Gaunpalika', 6, 49), 
    ('Kali Gandaki Gaunpalika', 7, 50), 
    ('Satyawoti Gaunpalika', 8, 50), 
    ('Chandrakot Gaunpalika', 8, 50), 
    ('Musikot Municipality', 9, 50), 
    ('Isma Gaunpalika', 6, 50), 
    ('Malika Gaunpalika', 8, 50), 
    ('Madane Gaunpalika', 7, 50), 
    ('Dhurkot Gaunpalika', 7, 50), 
    ('Resunga Municipality', 14, 50), 
    ('Gulmi Durbar Gaunpalika', 7, 50), 
    ('Chhatrakot Gaunpalika', 6, 50), 
    ('Ruruchhetra Gaunpalika', 6, 50), 
    ('Chhatradev Gaunpalika', 8, 51), 
    ('Malarani Gaunpalika', 9, 51), 
    ('Bhumikasthan Municipality', 10, 51), 
    ('Sandhikharka Municipality', 12, 51), 
    ('Panini Gaunpalika', 8, 51), 
    ('Shitaganga Municipality', 14, 51), 
    ('Rampur Municipality', 10, 52), 
    ('Purbakhola Gaunpalika', 6, 52), 
    ('Rambha Gaunpalika', 5, 52), 
    ('Baganaskali Gaunpalika', 9, 52), 
    ('Tansen Municipality', 14, 52), 
    ('Ribdikot Gaunpalika', 8, 52), 
    ('Rainadevi Chhahara Gaunpalika', 8, 52), 
    ('Tinau Gaunpalika', 6, 52), 
    ('Mathagadhi Gaunpalika', 8, 52), 
    ('Nisdi Gaunpalika', 7, 52), 
    ('Bardaghat Municipality', 16, 53), 
    ('Sunawal Municipality', 13, 53), 
    ('Ramgram Municipality', 18, 53), 
    ('Palhinandan Gaunpalika', 6, 53), 
    ('Sarawal Gaunpalika', 7, 53), 
    ('Pratapapur Gaunpalika', 9, 53), 
    ('Susta Gaunpalika', 5, 53), 
    ('Devdaha Municipality', 12, 54), 
    ('Butwal Sub-Metropolitian City', 19, 54), 
    ('Sainamaina Municipality', 11, 54), 
    ('Kanchan Gaunpalika', 5, 54), 
    ('Gaidahawa Gaunpalika', 9, 54), 
    ('Suddhodhan Gaunpalika', 7, 54), 
    ('Siyari Gaunpalika', 7, 54), 
    ('Tilottama Municipality', 17, 54), 
    ('Om Satiya Gaunpalika', 6, 54), 
    ('Rohini Gaunpalika', 7, 54), 
    ('Siddharthanagar Municipality', 13, 54), 
    ('Mayadevi Gaunpalika', 8, 54), 
    ('Lumbini Sanskritik Municipality', 13, 54), 
    ('Kotahimai Gaunpalika', 7, 54), 
    ('Sammarimai Gaunpalika', 7, 54), 
    ('Marchawari Gaunpalika', 7, 54), 
    ('Banganga Municipality', 11, 55), 
    ('Buddhabhumi Municipality', 10, 55), 
    ('Shivaraj Municipality', 11, 55), 
    ('Bijayanagar Gaunpalika', 7, 55), 
    ('Krishnanagar Municipality', 12, 55), 
    ('Maharajganj Municipality', 11, 55), 
    ('Kapilbastu Municipality', 12, 55), 
    ('Yasodhara Gaunpalika', 8, 55), 
    ('Mayadevi Gaunpalika', 8, 55), 
    ('Shuddhodhan Gaunpalika', 6, 55), 
    ('Bangalachuli Gaunpalika', 8, 56), 
    ('Ghorahi Sub-Metropolitian City', 19, 56), 
    ('Tulsipur Sub-Metropolitian City', 19, 56), 
    ('Shantinagar Gaunpalika', 7, 56), 
    ('Babai Gaunpalika', 7, 56), 
    ('Dangisharan Gaunpalika', 7, 56), 
    ('Lamahi Municipality', 9, 56), 
    ('Rapti Gaunpalika', 9, 56), 
    ('Gadhawa Gaunpalika', 8, 56), 
    ('Rajpur Gaunpalika', 7, 56), 
    ('Rapti Sonari Gaunpalika', 9, 57), 
    ('Kohalpur Municipality', 15, 57), 
    ('Baijanath Gaunpalika', 8, 57), 
    ('Khajura Gaunpalika', 8, 57), 
    ('Janaki Gaunpalika', 6, 57), 
    ('Nepalganj Sub-Metropolitian City', 23, 57), 
    ('Duduwa Gaunpalika', 6, 57), 
    ('Narainapur Gaunpalika', 6, 57), 
    ('Bansgadhi Municipality', 9, 58), 
    ('Barbardiya Municipality', 11, 58), 
    ('Thakurbaba Municipality', 9, 58), 
    ('Geruwa Gaunpalika', 6, 58), 
    ('Rajapur Municipality', 10, 58), 
    ('Madhuwan Municipality', 9, 58), 
    ('Gulariya Municipality', 12, 58), 
    ('Badhaiyatal Gaunpalika', 9, 58), 
    ('Dolpo Buddha Gaunpalika', 6, 59), 
    ('Shey Phoksundo Gaunpalika', 9, 59), 
    ('Jagadulla Gaunpalika', 6, 59), 
    ('Mudkechula Gaunpalika', 9, 59), 
    ('Tripurasundari Municipality', 11, 59), 
    ('Thulibheri Municipality', 11, 59), 
    ('Kaike Gaunpalika', 6, 59), 
    ('Chharka Tangsong Gaunpalika', 5, 59), 
    ('Mugumakarmarog Gaunpalika', 8, 60), 
    ('Chhayanath Rara Municipality', 13, 60), 
    ('Soru Gaunpalika', 10, 60), 
    ('Khatyad Gaunpalika', 10, 60), 
    ('Chankheli Gaunpalika', 5, 61), 
    ('Kharpunath Gaunpalika', 4, 61), 
    ('Simkot Gaunpalika', 7, 61), 
    ('Namkha Gaunpalika', 5, 61), 
    ('Sarkegad Gaunpalika', 7, 61), 
    ('Adanchuli Gaunpalika', 5, 61), 
    ('Tanjakot Gaunpalika', 4, 61), 
    ('Patarasi Gaunpalika', 6, 62), 
    ('Kanaka Sundari Gaunpalika', 7, 62), 
    ('Sinja Gaunpalika', 5, 62), 
    ('Chandannath Municipality', 9, 62), 
    ('Guthichaur Gaunpalika', 4, 62), 
    ('Tatopani Gaunpalika', 7, 62), 
    ('Tila Gaunpalika', 8, 62), 
    ('Hima Gaunpalika', 6, 62), 
    ('Palata Gaunpalika', 8, 63), 
    ('Pachal Jharana Gaunpalika', 8, 63), 
    ('Raskot Municipality', 8, 63), 
    ('Sanni Tribeni Gaunpalika', 8, 63), 
    ('Naraharinath Gaunpalika', 8, 63), 
    ('Khandachakra Municipality', 10, 63), 
    ('Tilagupha Municipality', 10, 63), 
    ('Mahawai Gaunpalika', 6, 63), 
    ('Shuva Kalika Gaunpalika', 7, 63), 
    ('Naumule Gaunpalika', 7, 64), 
    ('Mahabu Gaunpalika', 7, 64), 
    ('Thantikandh Gaunpalika', 5, 64), 
    ('Bhairabi Gaunpalika', 6, 64), 
    ('Aathbis Municipality', 8, 64), 
    ('Chamunda Bindrasaini Municipality', 8, 64), 
    ('Dullu Municipality', 12, 64), 
    ('Narayan Municipality', 10, 64), 
    ('Bhagawatimai Gaunpalika', 10, 64), 
    ('Dungeshwor Gaunpalika', 10, 64), 
    ('Gurans Gaunpalika', 10, 64), 
    ('Select', 10, 65), 
    ('Naumule Gaunpalika', 10, 65), 
    ('Mahabu Gaunpalika', 10, 65), 
    ('Bhairabi Gaunpalika', 10, 65), 
    ('Thantikandh Gaunpalika', 10, 65), 
    ('Aathbis Municipality', 10, 65), 
    ('Chamunda Bindrasaini Municipality', 10, 65), 
    ('Dullu Municipality', 5, 65), 
    ('Bhagawatimai Gaunpalika', 6, 65), 
    ('Dungeshwor Gaunpalika', 5, 65), 
    ('Gurans Gaunpalika', 7, 65), 
    ('Aathabisakot Municipality', 13, 66), 
    ('Sanibheri Gaunpalika', 10, 66), 
    ('Banphikot Gaunpalika', 9, 66), 
    ('Musikot Municipality', 13, 66), 
    ('Tribeni Gaunpalika', 9, 66), 
    ('Chaurjahari Municipality', 13, 66), 
    ('Darma Gaunpalika', 5, 67), 
    ('Kumakh Gaunpalika', 6, 67), 
    ('Banagad Kupinde Municipality', 11, 67), 
    ('Siddha Kumakh Gaunpalika', 4, 67), 
    ('Bagachour Municipality', 11, 67), 
    ('Chhatreshwori Gaunpalika', 6, 67), 
    ('Sharada Municipality', 14, 67), 
    ('Kalimati Gaunpalika', 6, 67), 
    ('Tribeni Gaunpalika', 5, 67), 
    ('Kapurkot Gaunpalika', 5, 67), 
    ('Simta Gaunpalika', 8, 68), 
    ('Chingad Gaunpalika', 5, 68), 
    ('Lekabeshi Municipality', 9, 68), 
    ('Gurbhakot Municipality', 13, 68), 
    ('Bheriganga Municipality', 12, 68), 
    ('Birendranagar Municipality', 15, 68), 
    ('Barahatal Gaunpalika', 9, 68), 
    ('Panchapuri Municipality', 10, 68), 
    ('Chaukune Gaunpalika', 9, 68), 
    ('Himali Gaunpalika', 6, 69), 
    ('Gaumul Gaunpalika', 5, 69), 
    ('Budhinanda Municipality', 9, 69), 
    ('Swamikartik Khapar Gaunpalika', 4, 69), 
    ('Jagannath Gaunpalika', 5, 69), 
    ('Badimalika Municipality', 8, 69), 
    ('Khaptad Chhededaha Gaunpalika', 6, 69), 
    ('Budhiganga Municipality', 9, 69), 
    ('Tribeni Municipality', 8, 69), 
    ('Saipal Gaunpalika', 4, 70), 
    ('Bungal Municipality', 10, 70), 
    ('Surma Gaunpalika', 4, 70), 
    ('Talkot Gaunpalika', 6, 70), 
    ('Masta Gaunpalika', 6, 70), 
    ('Jayaprithbi Municipality', 10, 70), 
    ('Chhabis Pathibhara Gaunpalika', 6, 70), 
    ('Durgathali Gaunpalika', 6, 70), 
    ('Kedarsyun Gaunpalika', 8, 70), 
    ('Bitthadchir Gaunpalika', 8, 70), 
    ('Thalara Gaunpalika', 8, 70), 
    ('Khaptad Chhanna Gaunpalika', 6, 70), 
    ('Byas Gaunpalika', 5, 71), 
    ('Duhun Gaunpalika', 4, 71), 
    ('Mahakali Municipality', 8, 71), 
    ('Naugad Gaunpalika', 5, 71), 
    ('Apihimal Gaunpalika', 5, 71), 
    ('Marma Gaunpalika', 5, 71), 
    ('Shailyashikhar Municipality', 8, 71), 
    ('Malikarjun Gaunpalika', 7, 71), 
    ('Lekam Gaunpalika', 5, 71), 
    ('Dilasaini Gaunpalika', 6, 72), 
    ('Dogada Kedar Gaunpalika', 7, 72), 
    ('Puchaundi Municipality', 9, 72), 
    ('Surnaya Gaunpalika', 7, 72), 
    ('Dasharathchand Municipality', 10, 72), 
    ('Pancheshwor Gaunpalika', 5, 72), 
    ('Shivanath Gaunpalika', 5, 72), 
    ('Melauli Municipality', 8, 72), 
    ('Patan Municipality', 9, 72), 
    ('Sigas Gaunpalika', 8, 72), 
    ('Nawadurga Gaunpalika', 4, 73), 
    ('Amargadhi Municipality', 10, 73), 
    ('Ajayameru Gaunpalika', 5, 73), 
    ('Bhageshwor Gaunpalika', 4, 73), 
    ('Parashuram Municipality', 11, 73), 
    ('Aalital Gaunpalika', 7, 73), 
    ('Ganyapdhura Gaunpalika', 4, 73), 
    ('Purbichouki Gaunpalika', 6, 74), 
    ('Sayal Gaunpalika', 5, 74), 
    ('Aadarsha Gaunpalika', 7, 74), 
    ('Shikhar Municipality', 10, 74), 
    ('Dipayal Silgadhi Municipality', 8, 74), 
    ('K.I. Singh Gaunpalika', 6, 74), 
    ('Bogatan Phudsil Gaunpalika', 6, 74), 
    ('Badi Kedar Gaunpalika', 4, 74), 
    ('Jorayal Gaunpalika', 5, 74), 
    ('Panchdebal Binayak Municipality', 8, 75), 
    ('Ramaroshan Gaunpalika', 6, 75), 
    ('Mellekh Gaunpalika', 7, 75), 
    ('Sanphebagar Municipality', 13, 75), 
    ('Chaurpati Gaunpalika', 6, 75), 
    ('Mangalsen Municipality', 13, 75), 
    ('Bannigadhi Jayagadh Gaunpalika', 5, 75), 
    ('Kamal bazar Municipality', 9, 75), 
    ('Dhakari Gaunpalika', 7, 75), 
    ('Turmakhand Gaunpalika', 7, 75), 
    ('Mohanyal Gaunpalika', 6, 76), 
    ('Chure Gaunpalika', 5, 76), 
    ('Godawari Municipality', 11, 76), 
    ('Gauriganga Municipality', 10, 76), 
    ('Ghodaghodi Municipality', 11, 76), 
    ('Bardagoriya Gaunpalika', 5, 76), 
    ('Lamki Chuha Municipality', 9, 76), 
    ('Janaki Gaunpalika', 8, 76), 
    ('Joshipur Gaunpalika', 6, 76), 
    ('Tikapur Municipality', 8, 76), 
    ('Bhajani Municipality', 8, 76), 
    ('Kailari Gaunpalika', 8, 76), 
    ('Dhangadhi Sub-Metropolitian City', 18, 76), 
    ('Krishnapur Municipality', 8, 77), 
    ('Shuklaphanta Municipality', 11, 77), 
    ('Bedkot Municipality', 9, 77), 
    ('Bhimdatta Municipality', 18, 77), 
    ('Dodhara Chandani Municipality', 9, 77), 
    ('Laljhadi Gaunpalika', 5, 77), 
    ('Punarbas Municipality', 10, 77), 
    ('Belouri Municipality', 9, 77), 
    ('Beldandi Gaunpalika', 4, 77);
    """)
    
    pass


def downgrade() -> None:
    pass

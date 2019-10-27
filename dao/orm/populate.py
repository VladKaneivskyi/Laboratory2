from dao.orm.model import *


db.session.query(Store_Have_Goods).delete()
db.session.query(Characteristic).delete()
db.session.query(Store).delete()
db.session.query(Result).delete()
db.session.query(Goods).delete()

Good1 = Goods(
    good_id=0,
    good_name ="Samsung",
    good_model ="S10")
Good2 = Goods(
    good_id=4,
    good_name="OnePlus",
    good_model="7 PRO")
Good3 = Goods(
    good_id=1,
    good_name="IPhone",
    good_model="11")
Good4 = Goods(
    good_id=2,
    good_name="Huawei",
    good_model="P30 PRO")
Good5 = Goods(
    good_id=3,
    good_name="Xiaomi",
    good_model="Mi9")


Charc1 = Characteristic(

    charac_name="RAM",
    charac_description="4Gb"
)
Charc6 = Characteristic(

    charac_name="RAM",
    charac_description="8Gb"
)
Charc2 = Characteristic(

    charac_name="Color",
    charac_description="black")
Charc7 = Characteristic(

    charac_name="Color",
    charac_description="yellow")

Charc3 = Characteristic(
    charac_name="Capacity",
    charac_description="64Gb")

Charc4 = Characteristic(

    charac_name="Display",
    charac_description="16:9")

Charc5 = Characteristic(

    charac_name="Front Camera",
    charac_description="12MP")


Store1 = Store(
    store_id = 2,
    store_name="Rozetka",
    store_link="https://rozetka.com.ua")
Store2 = Store(
    store_id = 1,
    store_name="Comfy",
    store_link="https://comfy.com.ua")
Store3 = Store(
    store_id = 4,
    store_name="Citrus",
    store_link="https://citrus.com.ua")
Store4 = Store(
    store_id = 3,
    store_name="Hotline",
    store_link="https://hotline.com.ua")
Store5 = Store(
    store_id = 0,
    store_name="Allo",
    store_link="https://allo.com.ua")

Result1 = Result(
    result_id =4,

)

Result2 = Result(
    result_id =0,
    )

Result3 = Result(
    result_id =3,
    )

Result4 = Result(
    result_id =2,
    )
Result5 = Result(
    result_id =1,
    )



# create relations
Good1.results.append(Result1)
Good2.results.append(Result2)
Good3.results.append(Result3)
Good4.results.append(Result4)
Good5.results.append(Result5)

Good1.store_id_fk.append(Store1)
Good1.store_id_fk.append(Store2)
Good1.store_id_fk.append(Store3)

Good2.store_id_fk.append(Store2)
Good2.store_id_fk.append(Store3)
Good2.store_id_fk.append(Store4)

Good3.store_id_fk.append(Store1)
Good3.store_id_fk.append(Store3)

Good4.store_id_fk.append(Store4)

Good5.store_id_fk.append(Store5)



Good1.characters.append(Charc1)
Good1.characters.append(Charc2)
Good1.characters.append(Charc3)
Good1.characters.append(Charc4)
Good1.characters.append(Charc5)


Good2.characters.append(Charc6)
Good2.characters.append(Charc7)
Good2.characters.append(Charc3)
Good2.characters.append(Charc4)
Good2.characters.append(Charc5)


Good3.characters.append(Charc3)
Good4.characters.append(Charc4)
Good5.characters.append(Charc5)


# insert into database
db.session.add_all([Result1,Result2,Result3,Result4,Result5])
db.session.add_all([Charc1,Charc2,Charc3,Charc4,Charc5])
db.session.add_all([Good1,Good2,Good3,Good4,Good5])
db.session.add_all([Store1,Store2,Store3,Store4,Store5])


db.session.commit()

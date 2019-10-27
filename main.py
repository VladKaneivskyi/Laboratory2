from flask import render_template, request, redirect, url_for
from forms.CharacteristicForm  import CharacteristicForm
from forms.EditCharacteristicForm  import EditCharacteristicForm
from forms.EditGoodsForm  import EditGoodsForm
from forms.EditStoreForm  import EditStoreForm
from forms.GoodsForm  import GoodsForm
from forms.StoreForm  import StoreForm
from dao.orm.populate import *
import plotly
import json
import plotly.graph_objs as go
from sqlalchemy.sql import func

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vlad16tank@localhost/NoSQL'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route('/all_characteristic', methods=['GET'])
def characteristic():

    result = db.session.query(Characteristic).all()

    return render_template('all_characteristic.html', result = result)


@app.route('/new_characteristic', methods=['GET','POST'])
def new_characteristic():

    form = CharacteristicForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_charactersitic_form.html', form=form, form_name="New characteristic", action="new_characteristic")
        else:
            new_characteristic= Characteristic(

                                charac_name=form.charac_name.data,
                                charac_description=form.charac_description.data

                            )

            db.session.add(new_characteristic)
            db.session.commit()


            return redirect(url_for('characteristic'))

    return render_template('new_charactersitic_form.html', form=form, form_name="New characteristic", action="new_characteristic")


'''
@app.route('/edit_characteristic/<string:charac_name>', methods=['GET', 'POST'])
def edit_characteristic(charac_name):

    form = EditCharacteristicForm()
    result = db.session.query(Characteristic).filter(Characteristic.charac_name == charac_name).one()

    if request.method == 'GET':

    
        form.charac_name.data = result.charac_name
        form.charac_description.data = result.charac_description



        return render_template('edit_characteristic_form.html', form=form, form_name='edit characteristic')
    elif request.method == 'POST':
        result.charac_id = form.charac_id.data
        result.charac_name = form.charac_name.data
        result.charac_description = form.charac_description.data



        db.session.commit()
        return redirect('/all_characteristic')
'''

@app.route('/delete_characteristic/<string:charac_name>/<string:charac_description>', methods=['GET', 'POST'])
def delete_characteristic(charac_name, charac_description):
    result = db.session.query(Characteristic).filter(Characteristic.charac_name == charac_name).filter(
        Characteristic.charac_description == charac_description).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_characteristic')

@app.route('/all_goods', methods=['GET'])
def goods():

    result = db.session.query(Goods).all()

    return render_template('all_goods.html', result = result)


@app.route('/new_goods', methods=['GET','POST'])
def new_goods():

    form = GoodsForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_goods_form.html', form=form, form_name="New goods", action="new_goods")
        else:
            new_goods= Goods(
                                good_id=form.good_id.data,
                                good_name=form.good_name.data,
                                good_model=form.good_name.data

                            )

            db.session.add(new_goods)
            db.session.commit()


            return redirect(url_for('goods'))

    return render_template('new_goods_form.html', form=form, form_name="New goods", action="new_goods")



@app.route('/edit_goods/<string:good_name>', methods=['GET', 'POST'])
def edit_goods(good_name):

    form = EditGoodsForm()
    result = db.session.query(Goods).filter(Goods.good_name == good_name).one()

    if request.method == 'GET':

        form.good_id.data = result.good_id
        form.good_name.data = result.good_name
        form.good_model.data = result.good_model



        return render_template('edit_goods_form.html', form=form, form_name='edit goods')
    elif request.method == 'POST':

        result.good_id = form.good_id.data
        result.good_name = form.good_name.data
        result.good_model = form.good_model.data


        db.session.commit()
        return redirect('/all_goods')


@app.route('/delete_goods/<string:good_name>', methods=['GET', 'POST'])
def delete_goods(good_name):
    result = db.session.query(Goods).filter(Goods.good_name == good_name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_goods')


@app.route('/all_store', methods=['GET'])
def store():

    result = db.session.query(Store).all()

    return render_template('all_store.html', result = result)


@app.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_store_form.html', form=form, form_name="New store", action="new_store")
        else:
            new_store = Store(
                store_id=form.store_id.data,
                store_name=form.store_name.data,
                store_link=form.store_link.data

            )

            db.session.add(new_store)
            db.session.commit()

            return redirect(url_for('store'))

    return render_template('new_store_form.html', form=form, form_name="New store", action="new_store")


@app.route('/edit_store/<string:store_name>', methods=['GET', 'POST'])
def edit_store(store_name):

    form = EditStoreForm()
    result = db.session.query(Store).filter(Store.store_name == store_name).one()

    if request.method == 'GET':

        form.store_id.data = result.store_id
        form.store_name.data = result.store_name
        form.store_link.data = result.store_link



        return render_template('edit_store_form.html', form=form, form_name='edit store')
    elif request.method == 'POST':

        result.store_id = form.store_id.data
        result.store_name = form.store_name.data
        result.store_link = form.store_link.data


        db.session.commit()
        return redirect('/all_store')
@app.route('/delete_store/<string:store_name>', methods=['GET', 'POST'])
def delete_store(store_name):
    result = db.session.query(Store).filter(Store.store_name == store_name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_store')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            Goods.good_name,
            func.count(Characteristic.charac_name).label('charac_name_count')
        ).
            outerjoin(Characteristic).
            group_by(Goods.good_name)
    ).all()

    query2 = (
        db.session.query(
            Goods.good_name,
            func.count(Store_Have_Goods.store_id_fk).label('store_count')
        ).
            outerjoin(Store_Have_Goods).
            group_by(Goods.good_name)
    ).all()

    name, charac_count = zip(*query1)
    bar = go.Bar(
        x=name,
        y=charac_count
    )

    name, store_count = zip(*query2)
    pie = go.Pie(
        labels=name,
        values=store_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)
    

if __name__ == "__main__":
    app.run(debug=True)





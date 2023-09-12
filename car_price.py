import pickle
import streamlit as st
from PIL import Image
path='C:/Users/silam/OneDrive/Desktop/model/'
rf_model = pickle.load(open(path + 'random_forest_regression_model.pkl', 'rb'))

def main():
    st.title("Selling Price Predictor ")
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price.. ")

    st.write('')
    st.write('')

    years = st.number_input('In which year car was purchased ?',1990, 2023, step=1, key ='year')
    total_years = 2023-years

    km_driven = st.number_input('What is distance completed by the car in Kilometers ?', 1000, 500000, step=500, key ='km_driven')
    engine = st.number_input('What is engine power by the car in CC ?', 150, 2500, step=10, key ='engine')
    mileage = st.number_input('What is mileage by the car in Kilometers ?', 10.0, 50.0, step=1.0, key ='mileage')
    max_power = st.number_input('What is max_power by the car in bhp ?', 1.0, 20.0, step=1.0, key ='max_power')
    seats=st.number_input('What is seats by the car in nos ?', 4.0, 8.0, step=1.0, key ='seats')
    owner_First_Owner= st.selectbox("The number of owners the car had previously ?", ('First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'), key='owner')
    
    if(owner_First_Owner=='First Owner'):
        owner_First_Owner=1
        owner_Second_Owner=0
        owner_Third_Owner=0
        owner_Test_Drive_Car=0
    elif(owner_First_Owner=='Scond Owner'):
        owner_First_Owner=0
        owner_Second_Owner=1
        owner_Third_Owner=0
        owner_Test_Drive_Car=0 
    elif(owner_First_Owner=='Third Owner'):
        owner_First_Owner=0
        owner_Second_Owner=0
        owner_Third_Owner=1
        owner_Test_Drive_Car=0
    elif(owner_First_Owner=='Test Drive Car'):
        owner_First_Owner=0
        owner_Second_Owner=0
        owner_Third_Owner=0
        owner_Test_Drive_Car=1  
    else:
        owner_First_Owner=0
        owner_Second_Owner=0
        owner_Third_Owner=0
        owner_Test_Drive_Car=0    

    fuel_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG','LPG'), key='fuel')
    if(fuel_Petrol=='Petrol'):
        fuel_Petrol=1
        fuel_Diesel=0
        fuel_CNG=0
    elif(fuel_Petrol=='Diesel'):
        fuel_Petrol=0
        fuel_Diesel=1
        fuel_CNG=0
    elif(fuel_Petrol=='CNG'):
        fuel_Petrol=0
        fuel_Diesel=0
        fuel_CNG=1
    else:
        fuel_Petrol=0
        fuel_Diesel=0
        fuel_CNG=0
    seller_type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual','Trustmark Dealer'), key='dealer')
    if(seller_type_Individual=='Individual'):
        seller_type_Individual=1
        seller_type_Dealer=0
    elif(seller_type_Individual=='Dealer'):
        seller_type_Individual=0
        seller_type_Dealer=1
    else:
        seller_type_Individual=0
        seller_type_Dealer=0

    transmission_Manual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(transmission_Manual=='Manual'):
        transmission_Manual=1
    else:
        transmission_Manual=0
    
    

    if st.button("Estimate Price", key='predict'):
        try:
            Model = rf_model  #get_model()
            prediction = Model.predict([[ km_driven, owner_First_Owner,owner_Second_Owner,owner_Third_Owner,owner_Test_Drive_Car, total_years, fuel_Diesel, fuel_Petrol,fuel_CNG, seller_type_Individual,seller_type_Dealer, transmission_Manual,mileage,max_power,seats,engine]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")
            



if __name__ == "__main__":
    main()



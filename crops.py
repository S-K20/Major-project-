def crop(crop_name):
    crop_data = {
    "wheat":["/static/images/wheat.jpg", "U.P., Punjab, Haryana, Rajasthan, M.P., Bihar", "Rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images/paddy.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "Kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images/barley.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "Rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images/maize.jpg", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "Kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images/bajra.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "Kharif", "Oman, Saudi ARabia, Israel, Japan"],
    "copra":["/static/images/copra.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal","Rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images/cotton.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat","Kharif", " China, Bangladesh, Egypt"],
    "masoor":["/static/images/masoor.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "Rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images/gram.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "Rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images/groundnut.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "Kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images/arhar.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "Kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images/sesamum.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "Rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images/jowar.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "Kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images/moong.jpg", "Rajasthan, Maharashtra, Andhra Pradesh", "Rabi", "Qatar, United States, Canada"],
    "niger":["/static/images/niger.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "Kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images/rape.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "Rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images/jute.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "Kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "Kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images/soyabean.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "Kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images/urad.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "Rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images/ragi.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "Kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images/sunflower.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "Rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images/sugarcane.jpg","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "Kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]
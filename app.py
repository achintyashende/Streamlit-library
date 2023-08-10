import streamlit as st

st.title('hello world !!')  # Title
st.header('Header')  # Header
st.subheader('Sub-header')  # SubHeader
st.text('Text')  # Text

st.markdown('# Hi')  # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success!')  # Success

st.info('Information!')  # Info

st.warning('Warning!')  # Warning

st.error('Error!')  # Error

st.exception(FileNotFoundError('Sorry we cant find your file.'))  # Exception

st.subheader('Help')
st.help(ZeroDivisionError)  # Help
st.help(FileNotFoundError)

st.subheader('Write')

st.write("range(1,10)")  # Write
st.write(range(1, 10))
st.write('1+2+3')
st.write(1 * 2 * 3)

st.subheader('Code')
st.code('x = 10\n'  # Code
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')  # Checkbox
if st.checkbox('Other'):  # Checkbox with Validation
    st.write("Why are you GAY!!🤨")

st.subheader('Radio Button')  # Radio Button
radioButton = st.radio('Select : ', ('Male', 'Female', 'Other'))
if radioButton == 'Male':
    st.write("Good 👍")
elif radioButton == 'Female':
    st.write("Women. ha ha!🤣🤣")
elif radioButton == 'Other':
    st.write("Why are you GAY!!🤨")

st.subheader('Select Box')  # SelectBox
selectBox = st.selectbox("Cities : ", ['Amravati', 'Agra', 'Chandigarh', 'Chennai', 'Delhi', 'Nagpur', 'Nashik'])
st.write("You've selected : ", selectBox)

st.subheader('MultiSelect Box')  # MultiSelectBox
multiSelBox = st.multiselect("Data Science : ", ['Data Analsis', 'Web Scraping', 'Machine Learning',
                                                 'Deep Learning', 'Natural Language Processing',
                                                 'Computer Vision', 'Image Processing'])
st.write("You selected : ", len(multiSelBox), 'courses')

st.subheader("Button")  # Button
if st.button('Click'):
    st.write('Thanks for clicking me')

st.subheader("Slider")  # Slider
vol = st.slider('Select the volume', 0, 100, step=1)
st.write('Volume is : ', vol)
if vol >= 80:
    st.write("Too much volume🤯 !!")

st.subheader("Text Input")  # Text-Input
username = st.text_input('Username : ')
password = st.text_input('Password : ', type='password')

st.subheader("Text Area")  # Text-Area
st.text_area('Write something interesting about yourself')

st.subheader("Input Number")  # Input-Number
st.number_input('Select your age', 18, 110)

st.subheader("Input Date")  # Input-Date
st.date_input('Date')

st.subheader("Input Time")  # Input-Time
st.time_input('Time')

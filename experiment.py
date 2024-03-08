import streamlit as st

page=st.session_state

if "page" not in page:
    page['page']=['main']
if "count" not in page:
    page['count']=0
    
next=st.button('Next page')
prev=st.button('Previous page')
if next:
    
    if len(page['page'])-1<=page['count']:    
        page['page'].append('next'+str(page['count']))
    page['count']+=1
    st.experimental_rerun()
if prev:
    page['count']-=1
    st.experimental_rerun()

if 'main'==page['page'][page['count']]:
        st.write("i am in main")
        
        
if 'next0'==page['page'][page['count']]:
        st.write("i am in main")
        st.write("i am in main")
        st.write("i am in main")
        
if 'next1'==page['page'][page['count']]:
        st.write("i am in main")
        st.write("i am in main")
        st.write("i am in main")
        st.write("i am in main")
    


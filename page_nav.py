from streamlit.components.v1 import html
import streamlit as st
import os 

# code reference: https://github.com/streamlit/streamlit/issues/4832

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

def next_page():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
    else:
        st.session_state.current_page += 1

# Create a function to navigate to the previous page
def prev_page():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
    else:
        st.session_state.current_page -= 1

def get_page(current_file_name, order): 
    current_file_name = current_file_name[2:-3]
    pages_directory = "pages/"
    
    # List all the files in the specified directory
    file_names = [f for f in os.listdir(pages_directory) if f.endswith('.py')]
    
    # Extract the names without the file extension
    page_names = [os.path.splitext(file)[0] for file in file_names]

    # sort page names 
    sorted_page_names = sorted(page_names)

    # get truncated page names 
    final_page_names = [sorted_page_name[2:] for sorted_page_name in sorted_page_names] 

    # get the index for the current file name 
    index = final_page_names.index(current_file_name)
    
    # get the name of the page to navigate to whether next or previous by index 
    if order == "next": 
        nav_page(final_page_names[index+1])
    if order == "previous":
        nav_page(final_page_names[index-1])

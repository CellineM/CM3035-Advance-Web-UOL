from django.http import HttpResponse
from django.urls import reverse

def home(request):
    html = f"""
    <html>
    <head>
        <title>Student Performance Data</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                text-align: center;
                padding: 20px;
            }}
            ul {{
                list-style-type: none;
                padding: 10;
            }}
            li {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
    <!--main title of the page-->
        <h1>Welcome to the Student Performance API</h1>
        <div class="container">
            <ul>
                <!-- The information to log in into the admin site-->
                <li class="endpoint">
                    <h2>Admin Information</h2>
                    <p><strong>Username: </strong>admin</p>
                    <p><strong>Email: </strong>awdAdmin@gmail.com</p>
                    <p><strong>Password: </strong>awdcm3035</p>
                    <a href="/admin/">http://localhost:8000/admin/</a>
                </li>

                <br/>

                <li class="endpoint">
                    <h2>POST - Create new record</h2>
                    <p>To create a new student record</p>
                    <a href="{reverse('create_record')}">http://localhost:8000/api/students/create/</a>
                </li>

                <br/>
                
                <li class="endpoint">
                    <h2>GET/PUT/DELETE - Latest Student Record</h2>
                    <p>Retrieve the latest student record for the user to delete or update if needed.</p>
                    <a href="{reverse('latest_record')}">http://localhost:8000/api/students/latest/</a>
                </li>
                
                <br/>
                
                <li class="endpoint">
                    <h2>GET - Average GPA according to age</h2>
                    <p>Retrieve the records for average GPA according to the ages of the students</p>
                    <a href="{reverse('ageGpa')}">http://localhost:8000/api/students/gpa/age/</a>
                </li>
              
                <br/>
                
                <li class="endpoint">
                    <h2>GET - High Parental Education and High GPA</h2>
                    <p>Only retrieve the students with high GPA where the parents have high education</p>
                    <a href="{reverse('parent_highGpa')}">http://localhost:8000/api/students/gpa/parent/</a>
                </li>
                
                <br/>
                
                <li class="endpoint">
                    <h2>GET - GPA results by Ethnicity</h2>
                    <p>Retrieve the average GPA results of the students based on their ethnicity</p>
                    <a href="{reverse('ethnic')}">http://localhost:8000/api/students/gpa/ethnic/</a>
                </li>
                
                <br/>
                
                <li class="endpoint">
                    <h2>GET - Full Details of the Students</h2>
                    <a href="{reverse('fullLists')}">http://localhost:8000/api/students/fullList/</a>
                </li>
                
                <br/>
                <br/>
                
                <h1>Additional Details</h1>

                <li class="endpoint">
                    <h2>Gender</h2>
                    <ul>
                        <li>0: Male</li>
                        <li>1: Female</li>
                    </ul>
                </li>

                <li class="endpoint">
                    <h2>Ethnicity</h2>
                    <ul>
                        <li>0: Caucasian</li>
                        <li>1: African American</li>
                        <li>2: Asian</li>
                        <li>3: Other</li>
                    </ul>
                </li>

            <li class="endpoint">
                <h2>Parental Education Codes</h2>
                <ul>
                    <li>0: None</li>
                    <li>1: High School</li>
                    <li>2: Some College</li>
                    <li>3: Bachelor's</li>
                    <li>4: Higher</li>
                </ul>
            </li>
            <br/>
            <li class="endpoint">
                <h2>Parental Support Codes</h2>
                <ul>
                    <li>0: None</li>
                    <li>1: Low</li>
                    <li>2: Moderate</li>
                    <li>3: High</li>
                    <li>4: Very High</li>
                </ul>
            </li>
            <br/>
            <li class="endpoint">
                <h2>Grade Class Codes</h2>
                <ul>
                    <li>0: 'A' (GPA >= 3.5)</li>
                    <li>1: 'B' (3.0 <= GPA < 3.5)</li>
                    <li>2: 'C' (2.5 <= GPA < 3.0)</li>
                    <li>3: 'D' (2.0 <= GPA < 2.5)</li>
                    <li>4: 'F' (GPA < 2.0)</li>
                </ul>
            </li>
                
            </ul>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


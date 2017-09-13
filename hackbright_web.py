"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grade_tuple = hackbright.get_grades_by_github(github)


    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grade_tuple=grade_tuple)

    return html

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)

@app.route("/project")
def project_search():
    """List information about the project."""


    title = request.args.get('title')
    project_tuple = hackbright.get_project_by_title(title)
    project_grades = hackbright.get_grades_by_title(title)

    return render_template("project_info.html",
                            project_tuple=project_tuple,
                            project_grades=project_grades)


@app.route("/student-search")
def student_search():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def get_create_student_form():
    """Display form for adding a student."""

    return render_template("create_student.html")


@app.route("/student-added", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    github = request.form.get('github')

    first, last, github = hackbright.make_new_student(first_name, last_name, github)

    return render_template("new_student_info.html", first=first, github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

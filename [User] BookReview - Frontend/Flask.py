from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("randomForm.html")


@app.route("/form", methods=['POST'])
def get_name():
    name = request.form['name']
    print("This idiot's name is", name)
    return render_template("randomForm.html")


@app.route("/review")
def review():
    '''
    Using dummy data for now. Fetch from DB next time.
    '''

    ''' Dummy Main Book '''
    title = "The Arsonist"
    cover = "https://www.booktopia.com.au/blog/wp-content/uploads/2018/12/the-arsonist.jpg"
    desc = "Sed iaculis posuere diam ut cursus. assa magna, vulputate nec bibendum nec, posuere nec lacus. Sed iaculis posuere diam ut cursus. assa magna, vulputate nec bibendum nec, posuere nec lacus. Sed iaculis posuere diam ut cursus. assa magna, vulputate nec bibendum nec, posuere nec lacus. Sed iaculis posuere diam ut cursus. assa magna, vulputate nec bibendum nec, posuere nec lacus."
    author = "Chloe Hooper"
    tags = ["Fantasy", "Romance", "Cookbooks"]

    main_book = {"title": title, "cover": cover,
                 "desc": desc, "author": author, "tags": tags}

    ''' Dummy reviews '''
    name1 = "Jane P."
    img1 = "https://media.istockphoto.com/photos/portrait-of-a-smiling-young-woman-picture-id905456806?k=6&m=905456806&s=612x612&w=0&h=PvYHS82wm1FlEh7_8Owj_OamqJfJ8g3igDrfbA4Xo7I="
    text1 = "Good Book!"
    summary1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget sapien sapien. Curabitur in metus urna. In hac habitasse platea dictumst. Phasellus eu sem sapien, sed vestibulum velit. Nam purus nibh, lacinia non faucibus"
    overall1 = 4
    review1 = {"name": name1, "img": img1, "text": text1,
               "summary": summary1, "overall": overall1}

    reviews = [review1, review1, review1, review1, review1, review1]

    ''' Dummy Related books '''
    cover1 = "https://marketplace.canva.com/MADSMNPt8uA/3/0/thumbnail_large/canva-green-beach-photo-book-cover-MADSMNPt8uA.jpg"
    title1 = "The Sun in His Eyes"
    author1 = "Eleanor Fitzgerald"
    tags1 = ["Sports", "Cookbooks", "Psychology", "Biography"]
    related1 = {"cover": cover1, "title": title1,
                "author": author1, "tags": tags1}

    relateds = [related1, related1, related1]

    return render_template("review-page.html", main=main_book, reviews=reviews, relateds=relateds)


@app.route("/review", methods=["POST"])
def submit_review():
    '''
    Get the header and review from review form and do something upon submit
    '''
    text = request.form['reviewText']  # the short one
    summary = request.form['reviewSummary']  # the long one
    pass  # do something here


@app.route("/history")
def login():
    ''' 
    Using dummy data for now. Fetch from DB next time.
    '''
    b1 = "Harry Potter"
    c1 = "https://img1-placeit-net.s3-accelerate.amazonaws.com/uploads/stage/stage_image/39885/large_thumb_book-cover-horror-novel-527.jpg"
    a1 = "A. Dinh"
    tags1 = ["Art", "Cookbooks"]

    b2 = "Rich Dad Poor Dad"
    c2 = "https://img2-placeit-net.s3-accelerate.amazonaws.com/uploads/stage/stage_image/37837/large_thumb_stage.jpg"
    a2 = "B. Dinh"
    tags2 = ["Self Help", "Thriller", "Graphic Novels"]

    b3 = "Lord of The Rings"
    c3 = "https://i.pinimg.com/236x/82/79/74/827974d98ed5dabfbeecbdae890caebf.jpg"
    a3 = "C. Dinh"
    tags3 = ["Business", "Fiction", "Nonfiction"]

    books = [b1, b2, b3]
    covers = [c1, c2, c3]
    author = [a1, a2, a3]
    tags = [tags1, tags2, tags3]

    return render_template("history.html", count=len(books), books=books, covers=covers, author=author, tags=tags)


@app.route("/add-a-book")
def add_a_book():
    return render_template("add-a-book.html")


@app.route("/add-a-book", methods=['POST'])
def submit_book_info():
    '''
    Get the book info from add-a-book form and do something upon submit
    '''
    ClientName = request.form['ClientName']
    ClientEmail = request.form['ClientEmail']
    BookCat = request.form["BookCat"]
    BookName = request.form["BookName"]
    BookAuthor = request.form["BookAuthor"]
    MoreAbtBook = request.form["MoreAbtBook"]

    # print(MoreAbtBook)

    pass  # do something here
    return render_template("thank-you.html")


if __name__ == "__main__":
    app.run(debug=True)
else:
    print("Something wrong")
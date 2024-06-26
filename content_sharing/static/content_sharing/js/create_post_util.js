/**
 * CreatePostUtil
 * Handles the creation of posts by
 * sending social media content to Django's
 * backend for processing.
 * 
 * @param postContentTextboxID
 */
class CreatePostUtil {

    constructor(postContentTextboxID) {
        this.postForm = document.getElementById('create-post');
        this.postForm.addEventListener('submit', event => {
            event.preventDefault();
            const postContentElement = document.getElementById(postContentTextboxID);
            this.sendPostContent(postContentElement);
        })
    }

    /**
     * Event activated for sending
     * social media content to the Django backend
     * for post creation.
     * @param {Element} postContentElement 
     */
    sendPostContent(postContentElement) {
        if (postContentElement.value.length > 0) {
            fetch("/api/create_post", {
                "method": "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": this._getCookie('csrftoken')
                },
                body: 'content=' + encodeURIComponent(postContentElement.value)
            })
            .then(response => {
                return response.json().then(data => {
                    if (response.status === 201) {
                        let errorList = document.getElementById('post-form-errors');
                        errorList.innerHTML = "<ul></ul>";
                        return data;
                    } else {
                        throw { ...data };
                    }
                })
            })
            .then(data => {
                this._createPost(data);
            })
            .catch(response => {
                let errorMessage = document.createElement('li');
                errorMessage.textContent = response.failure;
                
                const errorList = document.getElementById('post-form-errors');
                errorList.append(errorMessage);
            });
        } else {
            alert('Something went wrong, please ensure your textbox is not empty.');
        }
    }

    /**
     * Retrieves cookies from the browser.
     * @param {string} name 
     * @returns 
     */
    _getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    /**
     * Consumes the JSON of the AJAX sent/recieved
     * from the backend.
     * @param {Response} json 
     */
    _createPost(json) {
        const posts = document.getElementById('posts');
        const post = document.createElement('aside');
        post.classList.add('post');
        post.append(this._createPostMetaData(json.profile_picture, json.creator, json.created));
        post.append(this._createContentElement(json.content));
        posts.insertBefore(post, posts.firstChild);
    }

    /**
     * Generates the meta data of the post
     * with information such as the image.
     * @param {string} profilePicturePath 
     * @returns 
     */
    _createPostMetaData(profilePicturePath, username, date) {
        const header = document.createElement('header');
        header.classList.add('post-info');
        header.append(this._createProfilePictureElement(profilePicturePath));
        header.append(this._createPostCreationInfo(username, date));
        return header;
    }

    _createProfilePictureElement(profilePicture) {
        const imageElement = document.createElement('img');
        imageElement.src = profilePicture;
        imageElement.alt = 'The profile picture of the user for their profile';
        return imageElement;
    }

    /**
     * Creates a container with post creation info
     * to add it to the post meta data container.
     * @param {string} creator 
     * @param {string} date 
     * @returns 
     */
    _createPostCreationInfo(creator, date) {
        const postCreation = document.createElement('div');
        postCreation.classList.add('post-creation');
        postCreation.append(this._createUsernameElement(creator));
        postCreation.append(document.createElement('br'));
        postCreation.append(this._createDateElement(date));
        return postCreation;
    }

    _createUsernameElement(creator) {
        const usernameElement = document.createElement('em');
        usernameElement.textContent = creator;
        return usernameElement;
    }

    _createDateElement(date) {
        const dateElement = document.createElement('small');
        dateElement.textContent = date;
        return dateElement;
    }

    _createContentElement(content) {
        const contentElement = document.createElement('p');
        contentElement.classList.add('post-contents');
        contentElement.textContent = content;
        return contentElement;
    }
}

new CreatePostUtil('content-to-be-posted');
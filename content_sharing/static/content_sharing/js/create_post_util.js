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
}

new CreatePostUtil('content-to-be-posted');
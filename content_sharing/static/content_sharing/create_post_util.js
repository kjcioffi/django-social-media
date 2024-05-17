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
        try {
            let request;
            if (postContentElement.value.length > 0) {
                request = fetch("/api/create_post", {
                    "method": "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-CSRFToken": this._getCookie('csrftoken')
                    },
                    body: 'content=' + postContentElement.value
                });
            } else {
                alert('Something went wrong, please ensure your textbox is not empty.');
            }

        } catch(error) {
            console.error('There was a problem with post creation: ', error.message);
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
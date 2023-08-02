const {createApp} = Vue
const app = createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            page: 1,
            page_size: 10,
            post_data: {
                count: 0,
                next: null,
                previous: null,
                results: []
            },
        }
    },

    methods: {
        async getData(page) {
            try {
                const response = await axios.get(
                    "/api/post/posts?page=" + page + "&page_size=" + this.page_size
                );
                this.post_data = response.data;
            } catch (error) {
                console.log(error);
            }
        }
    },

    beforeMount() {
        this.getData(this.page);
    }
})
app.mount('#app')
app.config.globalProperties.$filters = {
    str_limit(value, size) {
        if (!value) return '';
        value = value.toString();

        if (value.length <= size) {
            return value;
        }
        return value.substring(0, size) + '...';
    }
}
<template>
    <!-- 添加食谱页面 -->
    <div>
        <navbar />
        <main class="container my-5">
            <div class="row">
                <div class="col-12 text-center my-3">
                    <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
                </div>
                <div class="col-md-6 mb-4">
                    <img
                      v-if="preview"
                      class="img-fluid"
                      style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
                      :src="preview"
                      alt
                    >
                    <img
                      v-else
                      class="img-fluid"
                      style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
                      src="@/static/images/placeholder.png"
                    >
                </div>
                <div class="col-md-4">
                    <form @submit.prevent="submitRecipe">
                        <div class="form-group">
                            <label for>食谱名称</label>
                            <input type="text" class="form-control" v-model="recipe.name">
                        </div>
                        <div class="form-group">
                            <label for>食材</label>
                            <input v-model="recipe.ingredients" type="text" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for>图片</label>
                            <input type="file" name="file" @change="onFileChange">
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for>难度</label>
                                    <select v-model="recipe.difficulty" class="form-control">
                                        <option value="Easy">容易</option>
                                        <option value="Medium">中等</option>
                                        <option value="Hard">困难</option>
                                    </select>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for>
                                        制作时间
                                        <small>(分钟)</small>
                                    </label>
                                    <input v-model="recipe.prep_time" type="number" class="form-control">
                                </div>
                            </div>
                        </div>
                        <div class="form-group mb-3">
                            <label for>制作指南</label>
                            <textarea v-model="recipe.prep_guide" class="form-control" rows="8"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">提交</button>
                    </form>
                </div>
            </div>
        </main>
        <myFooter />
    </div>
</template>
  
<script>
import navbar from '~/components/navbar.vue';
import myFooter from "~/components/myFooter.vue";

export default {
  components: { navbar, myFooter },
    head() {
        return { title: "Add Recipe" };
    },
    data() {
        return {
            recipe: {
                name: "",
                picture: "",
                ingredients: "",
                difficulty: "",
                prep_time: null,
                prep_guide: "",
                owner: "",
            },
            owner: "",
            preview: "",
        };
    },
    mounted() {
        this.owner = localStorage.getItem('username');
    },
    methods: {
        onFileChange(e) {
            let files = e.target.files || e.dataTransfer.files;
            if (!files.length) {
                return;
            }
            this.recipe.picture = files[0];
            this.createImage(files[0]);
        },
        createImage(file) {
            let reader = new FileReader();
            let vm = this;
            reader.onload = e => {
                vm.preview = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        async submitRecipe() {
            const config = {
                headers: { "content-type": "multipart/form-data" }
            };
            this.recipe.owner = this.owner;
            let formData = new FormData();
            for (let data in this.recipe) {
                console.log(data);
                formData.append(data, this.recipe[data]);
            }
            console.log(formData);
            try {
                let response = await this.$axios.$post("/api/recipes/", formData, config);
                this.$router.push("/recipes/");
            } catch (e) {
                let code = e.response.status;
                if (code == 400) {
                    alert('请将食谱填写完整！')
                    location.reload()
                    this.$router.go(0)
                }
                console.log(e.response);
            }
        }
    }
};
</script>
  
<style scoped>
</style>
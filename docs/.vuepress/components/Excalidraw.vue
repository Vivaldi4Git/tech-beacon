<template>
  <div class="excalidraw-wrapper" ref="excalidrawWrapper"></div>
</template>

<script>
export default {
  name: 'Excalidraw',
  props: {
    file: {
      type: String,
      required: true
    }
  },
  mounted() {
    // 动态加载 Excalidraw 文件
    fetch(`/drawings/${this.file}`)
      .then(response => response.json())
      .then(data => {
        const App = window.Excalidraw.default;
        const excalidrawAPI = new App({
          container: this.$refs.excalidrawWrapper,
          initialData: data,
          viewModeEnabled: true
        });
      });
  }
}
</script>

<style>
.excalidraw-wrapper {
  height: 500px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
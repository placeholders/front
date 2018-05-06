<template>
	<div class="uk-margin" uk-margin>
        <label :for="inputId">{{ labelText }}:</label>
        <input
            class="uk-input"
            :problemtitle="inputProblemtitle"
            :inputtextresume="inputTextresume"
            v-bind:value="value"
            v-on:input="$emit('input', $event.target.value)"
            />
    </div>
</template>

<script>
export default {
  props:{
      value: String,
      Problemtitle: {
          type: String,
          default: "text",
      },
      : String,
      labelText: {
          type: String,
          required: true,
      }
  }
}
</script>


<style type="text/css">
</style>

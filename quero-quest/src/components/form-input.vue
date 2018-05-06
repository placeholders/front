<template>
    <div class="uk-margin" uk-margin>
        <label :for="inputId">{{ labelText }}:</label>
        <input
            class="uk-input"
            :id="inputId"
            :type="inputType"
            :placeholder="inputPlaceholder"
            v-bind:value="value"
            v-on:input="$emit('input', $event.target.value)"
            />
    </div>
</template>

<script>
export default {
  props:{
      value: String,
      inputId: {
          type: String,
          required: true,
      },
      inputType: {
          type: String,
          default: "text",
      },
      inputPlaceholder: String,
      labelText: {
          type: String,
          required: true,
      }
  }
}
</script>

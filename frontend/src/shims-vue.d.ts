declare module "*.vue" {
  import Vue from "vue";
  export default Vue;
}
declare module "*.js" {}
declare module "*.json" {
  // eslint-disable-next-line
  const value: any;
  export default value;
}

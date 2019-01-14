const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin")

module.exports = {

    mode: "development",

    // define entry points
    entry: {
        app: "./UI/static/js/main.js",
        signup: "./UI/static/js/signup.js",
        signin: "./UI/static/js/signin.js",
        dashboard: "./UI/static/js/dashboard.js",
        addParcel: "./UI/static/js/addParcel.js",
        contents: "./UI/static/js/contents.js",
        editParcel: "./UI/static/js/editParcel.js"
    },
    // define output point
    output:{
        path: path.resolve(__dirname, "UI/static/dist"),
        filename: "[name].min.js",
        // publicPath: "/dist"
    },
    module: {
        rules:[{
            test:/\.js$/,
            exclude:/node_modules/,
            use:[{
                loader:"babel-loader",
                options:{
                    presets:["env"]
                }
            }]
        },
        {
            test:/\.css$/,
            use:[
                "style-loader",
                "css-loader"
            ]
        },
        {
            test:/\.html$/,
            use:[ "html-loader"]
        },
        {
            test:/\.(jpg | png)$/,
            use:[
                {
                    loader: "file-loader",
                    options:{
                        name:"[name].[ext]",
                        outputPath:"/images/",
                        publicPath:"/images/"
                    }
                }
                
            ]
        }
]
    }
}
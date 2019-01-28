const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin")
const CleanWebpackPlugin = require("clean-webpack-plugin")
const ExtractTextPlugin = require("extract-text-webpack-plugin")

module.exports = {

    mode: "development",

    // define entry points
    entry: {
        app: "./UI/static/js/main.js",
        signup: "./UI/static/js/signup.js",
        signin: "./UI/static/js/signin.js",
        dashboard: "./UI/static/js/dashboard.js",
        profile: "./UI/static/js/profile.js",
        addParcel: "./UI/static/js/addParcel.js",
        contents: "./UI/static/js/contents.js",
        editOrder: "./UI/static/js/editOrder.js"
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
            use:ExtractTextPlugin.extract({
                fallback:"style-loader",
                use:["css-loader"],
                publicPath: "/dist"
            })
        },
        {
            test:/\.html$/,
            use:[ "html-loader"]
        },
        {
            test:/\.(jpg|png)$/,
            use:[
                {
                    loader: "file-loader",
                    options:{
                        name:"[name].[ext]",
                        outputPath:"images/",
                        publicPath:"images/"
                    }
                }
                
            ]
        }
    ]
    },
    
    plugins: [
        new ExtractTextPlugin({
            filename: "app.css",
            // disabled: false,
            allChunks:true
        }),
        new HtmlWebpackPlugin({
            title: "SendIT :: Parcel Delivery Service",
            template: "UI/index.html"
        }),
        new CleanWebpackPlugin(["UI/static/dist"])
    ]
}

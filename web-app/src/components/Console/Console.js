import Editor from "@monaco-editor/react";

const defaultOptions = {
    selectOnLineNumbers: true,
    roundedSelection: false,
    readOnly: false,
    cursorStyle: 'line',
    theme: 'vs-dark',
    minimap: {
        enabled: false
    },
};


const readOnlyOptions = {
    selectOnLineNumbers: true,
    roundedSelection: false,
    readOnly: true,
    cursorStyle: 'line',
    theme: 'vs-dark',
    minimap: {
        enabled: false
    }
}

export const Console = ({ children, readOnly, code = '', setCode }) => {
    let options = readOnly ? readOnlyOptions : defaultOptions;
    console.log(options)
    return (
        <div className='col d-flex flex-column justify-content-evenly'>
            <Editor
                theme="vs-dark"
                defaultLanguage="rust"
                value={code}
                onChange={setCode}
                options = {options}
            />

            {children}
        </div>
    )
}
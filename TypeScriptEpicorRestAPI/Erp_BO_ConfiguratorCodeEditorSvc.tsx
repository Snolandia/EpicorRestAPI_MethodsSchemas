import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ConfiguratorCodeEditorSvc
// Description: Configurator code editor service
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method BuildCodeEditorOptions
   Description: retrieves the Available Options for the code editor
   OperationID: BuildCodeEditorOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCodeEditorOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCodeEditorOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCodeEditorOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/BuildCodeEditorOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewConfiguratorCodeEditor
   Description: get a new parameters row
   OperationID: GetNewConfiguratorCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConfiguratorCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConfiguratorCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConfiguratorCodeEditor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/GetNewConfiguratorCodeEditor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param codeLanguage
      @param ConfiguratorCodeEditorTS
   */  
export interface BuildCodeEditorOptions_input{
      /**  The code language to construct the code editor  */  
   codeLanguage:string,
   ConfiguratorCodeEditorTS:Erp_Tablesets_ConfiguratorCodeEditorTableset[],
}

export interface BuildCodeEditorOptions_output{
parameters : {
      /**  output parameters  */  
   ConfiguratorCodeEditorTS:Erp_Tablesets_ConfiguratorCodeEditorTableset[],
}
}

export interface Erp_Tablesets_CodeEditorPCFuncParamRow{
   ParameterName:string,
   ParameterType:string,
   Modifier:string,
   DefaultValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCInputsRow{
   InputName:string,
   InputType:string,
   DataType:string,
   PcDynLstCount:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigUDCodEditorRow{
   Company:string,
   ConfigID:string,
   FunctionName:string,
   MethodDeclaration:string,
   MethodToolTip:string,
   DataType:string,
      /**  The tokenized text used for the expression builder.  */  
   TokenizedText:string,
   MethodType:string,
   CodeEditorText:string,
   ExcludeFromExpressionBuilder:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfiguratorCodeEditorRow{
   Company:string,
   ConfigID:string,
   RetrieveExpVars:boolean,
      /**   None -> do not retrieve UD Methods (string.empty = none)
Both -> retrieve client and server
Client -> retrieve client only
Server -> retrieve server only  */  
   UDMethodFunctionType:string,
   FromUDMethods:boolean,
   DedicatedTenancy:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfiguratorCodeEditorTableset{
   ConfiguratorCodeEditor:Erp_Tablesets_ConfiguratorCodeEditorRow[],
   CodeEditorPCFuncParam:Erp_Tablesets_CodeEditorPCFuncParamRow[],
   CodeEditorPCInputs:Erp_Tablesets_CodeEditorPCInputsRow[],
   ConfigUDCodEditor:Erp_Tablesets_ConfigUDCodEditorRow[],
   PcExpVar:Erp_Tablesets_PcExpVarRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcExpVarRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Tokenized Text used by the expression builder.  */  
   TokenizedText:string,
   CodeEditorText:string,
   AlternateText:string,
   Approved:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param companyID
      @param configID
      @param ConfiguratorCodeEditorTS
   */  
export interface GetNewConfiguratorCodeEditor_input{
      /**  Company ID  */  
   companyID:string,
      /**  Configuration ID  */  
   configID:string,
   ConfiguratorCodeEditorTS:Erp_Tablesets_ConfiguratorCodeEditorTableset[],
}

export interface GetNewConfiguratorCodeEditor_output{
parameters : {
      /**  output parameters  */  
   ConfiguratorCodeEditorTS:Erp_Tablesets_ConfiguratorCodeEditorTableset[],
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}


import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlRepackReclassPCIDSvc
// Description: 
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method Init
   Description: for unit testing
   OperationID: Init
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Init(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Init_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/Init", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Init_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetSourcePCID
   Description: Sets the entered PCID as the source container if valid
   OperationID: SetSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSourcePCID(requestBody:SetSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/SetSourcePCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreSetPkgControlRepackReclassPCID
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
inputs the target PCID or clicks the print button and the source qty > 0,
and before calling any update method that could generate PartTran.
   OperationID: PreSetPkgControlRepackReclassPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreSetPkgControlRepackReclassPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetPkgControlRepackReclassPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSetPkgControlRepackReclassPCID(requestBody:PreSetPkgControlRepackReclassPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreSetPkgControlRepackReclassPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/PreSetPkgControlRepackReclassPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreSetPkgControlRepackReclassPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RepackReclassPCID
   Description: Validates the target PCID and performs the repack based on the qty in the target PkgControlStageItem records.
   OperationID: RepackReclassPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RepackReclassPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RepackReclassPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RepackReclassPCID(requestBody:RepackReclassPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RepackReclassPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/RepackReclassPCID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RepackReclassPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadDefaultPrinter
   Description: Loads the first active printer with the lowest DisplaySequence that is defined for the "PKG-RPK" type.
   OperationID: LoadDefaultPrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDefaultPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadDefaultPrinter(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadDefaultPrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/LoadDefaultPrinter", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LoadDefaultPrinter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePrinter
   Description: Validates that the printer is active and exists for the "PKG-RPK" type.
   OperationID: ValidatePrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePrinter(requestBody:ValidatePrinter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/ValidatePrinter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePrinter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateNewPCIDQtyRemaining
   Description: Generates a new PCID for the remaining source PCID qty in preparation for printing the new label for the source; also updates any PkgControlSplitMerge and PkgControlStageHeader OriginalSourcePCID from old to the new PCID generated
   OperationID: GenerateNewPCIDQtyRemaining
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateNewPCIDQtyRemaining_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewPCIDQtyRemaining_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNewPCIDQtyRemaining(requestBody:GenerateNewPCIDQtyRemaining_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateNewPCIDQtyRemaining_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/GenerateNewPCIDQtyRemaining", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateNewPCIDQtyRemaining_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageCodeAllocNegQty(requestBody:CheckPackageCodeAllocNegQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPackageCodeAllocNegQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/CheckPackageCodeAllocNegQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPackageCodeAllocNegQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipNewPCID
      @param ipPackageCode
      @param ipQty
   */  
export interface CheckPackageCodeAllocNegQty_input{
   ipNewPCID:string,
   ipPackageCode:string,
   ipQty:number,
}

export interface CheckPackageCodeAllocNegQty_output{
parameters : {
      /**  output parameters  */  
   opWarning:string,
   opAction:string,
   opAllocWarning:string,
   opAllocAction:string,
}
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlRepackReclassPCIDRow{
      /**  Indicates if a new label has been printed for the source PCID after repack/reclass has taken place.  */  
   HasBeenPrinted:boolean,
      /**  Used as the primary key for the temp table  */  
   Seq:number,
      /**  The LPC status for the source PCID  */  
   SourceLPCStatus:string,
      /**  The source PCID for the repack/reclass  */  
   SourcePCID:string,
   SourceStatus:string,
      /**  UOM for the source Quantity  */  
   SourceUOM:string,
      /**  Target PCID  */  
   TargetPCID:string,
      /**  Total quantity of the PkgControlItem associated with the source PCID  */  
   SourceQuantity:number,
      /**  Holds any message returned from the legal number generation.  */  
   LegalNumberMessage:string,
      /**  The warehouse code for the transaction (comes from the source PkgControlHeader)  */  
   WarehouseCode:string,
   ContainerQtyMessage:string,
   PkgCode:string,
      /**  Indicates if a new label has been generated for the source PCID after partial repack/reclass has taken place.  */  
   RemainingPCIDGenerated:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlRepackReclassPCIDTableset{
   PkgControlRepackReclassPCID:Erp_Tablesets_PkgControlRepackReclassPCIDRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param printPCIDLabel
      @param pcidPrinter
   */  
export interface GenerateNewPCIDQtyRemaining_input{
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset[],
      /**  True/False indicates if the new label should be printed  */  
   printPCIDLabel:boolean,
      /**  User selected printer  */  
   pcidPrinter:string,
}

export interface GenerateNewPCIDQtyRemaining_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset,
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

export interface Init_output{
}

export interface LoadDefaultPrinter_output{
parameters : {
      /**  output parameters  */  
   pcidPrinter:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreSetPkgControlRepackReclassPCID_input{
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset[],
}

export interface PreSetPkgControlRepackReclassPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipNewPCID
      @param ds
   */  
export interface RepackReclassPCID_input{
      /**  target PCID  */  
   ipNewPCID:string,
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset[],
}

export interface RepackReclassPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlRepackReclassPCIDTableset,
}
}

   /** Required : 
      @param ipPCID
   */  
export interface SetSourcePCID_input{
      /**  Source PCID  */  
   ipPCID:string,
}

export interface SetSourcePCID_output{
   returnObj:Erp_Tablesets_PkgControlRepackReclassPCIDTableset[],
}

   /** Required : 
      @param iPCIDPrinter
   */  
export interface ValidatePrinter_input{
      /**  User selected printer  */  
   iPCIDPrinter:string,
}

export interface ValidatePrinter_output{
parameters : {
      /**  output parameters  */  
   opPCIDPrinter:string,
}
}


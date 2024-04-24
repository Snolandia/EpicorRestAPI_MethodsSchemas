import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartBinSearchSvc
// Description: Searches plants, warehouses, and part bins based on input parameters.
PartOnHandWhse was used as a template.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", {
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
   Summary: Invoke method CheckBin
   Description: Validate the bin and warehouse for the current plant..
   OperationID: CheckBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/CheckBin", {
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
   Summary: Invoke method GetBinContents
   Description: Gets a listing of parts in a particular whse/bin.
   OperationID: GetBinContents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBinContents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBinContents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBinContents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetBinContents", {
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
   Summary: Invoke method GetFullBinSearch
   Description: Gets the dataset of bins, in difference with GetPartBinSearch, this one includes All bins whether they have
a dimension or lot number or neither of both.
   OperationID: GetFullBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFullBinSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetFullBinSearch", {
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
   Summary: Invoke method GetInventoryAttributeValues
   Description: Create InventoryDynAttrValues table and populate it with inventory attribute values
   OperationID: GetInventoryAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryAttributeValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetInventoryAttributeValues", {
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
   Summary: Invoke method GetInventoryAttributeValuesOutDS
   OperationID: GetInventoryAttributeValuesOutDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryAttributeValuesOutDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryAttributeValuesOutDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryAttributeValuesOutDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetInventoryAttributeValuesOutDS", {
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
   Summary: Invoke method GetPartBinByLotAndPlant
   Description: Gets the warehouse/bin information for a specific lot, filtered by plant
   OperationID: GetPartBinByLotAndPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinByLotAndPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinByLotAndPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartBinByLotAndPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetPartBinByLotAndPlant", {
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
   Summary: Invoke method GetPartBinByLot
   Description: Gets the warehouse/bin information for a specific lot.
   OperationID: GetPartBinByLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinByLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinByLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartBinByLot(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetPartBinByLot", {
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
   Summary: Invoke method GetPartBinSearch
   Description: Gets the dataset of warehouses and bins for a Part.
If a change is made to this method the same change should be applied to
the GetSpecificBinSearch method.
   OperationID: GetPartBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartBinSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetPartBinSearch", {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetSpecificBinSearch
   Description: Gets the dataset of warehouses and bins for a Part.
If a change is made to this method the same change should be applied to
the GetPartBinSearch method.
   OperationID: GetSpecificBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecificBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecificBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSpecificBinSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/GetSpecificBinSearch", {
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
   Summary: Invoke method FindPart
   Description: Invokes Internal.Lib.FindPart which checks for the existence of a part.
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/FindPart", {
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
      @param whseCode
      @param binNum
   */  
export interface CheckBin_input{
      /**  The Warehouse.  */  
   whseCode:string,
      /**  The Bin.  */  
   binNum:string,
}

export interface CheckBin_output{
parameters : {
      /**  output parameters  */  
   errMsg:string,
}
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
   DataTableID:string,
   UniqueTableID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartBinSearchRow{
      /**  Company  */  
   Company:string,
      /**  Part number.  */  
   PartNum:string,
      /**  Plant  */  
   Plant:string,
      /**  Warehouse code.  */  
   WhseCode:string,
      /**  Bin number.  */  
   BinNum:string,
      /**  Lot number.  */  
   LotNumber:string,
      /**  Dimension code.  */  
   DimCode:string,
      /**  Quantity on hand for the bin.  */  
   QtyOnHand:number,
      /**  Part description  */  
   PartDesc:string,
      /**  Plant name.  */  
   PlantName:string,
      /**  Warehouse code description.  */  
   WhseCodeDesc:string,
      /**  Bin description.  */  
   BinDesc:string,
      /**  Lot number description.  */  
   LotNumberDesc:string,
      /**  Part dimension description.  */  
   DimCodeDesc:string,
      /**  Non nettable flag from WhseBin  */  
   NonNettable:boolean,
   IUM:string,
      /**  Bin Type  */  
   BinType:string,
   ContractID:string,
      /**  PCID  */  
   PCID:string,
      /**  Determines if the Part Bin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Allocated quantity for the bin  */  
   QtyAllocated:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartBinSearchTableset{
   PartBinSearch:Erp_Tablesets_PartBinSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  Entered Part Number  */  
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param whseCode
      @param binNum
   */  
export interface GetBinContents_input{
      /**  The Warehouse is required.  */  
   whseCode:string,
      /**  A specific Bin.  Required.  */  
   binNum:string,
}

export interface GetBinContents_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
}

   /** Required : 
      @param partNum
      @param whseCode
      @param consolidateInvAttributes
   */  
export interface GetFullBinSearch_input{
      /**  Part number.  */  
   partNum:string,
      /**  The Warehouse can be for a specific warehouse
            or null for all warehouses.  */  
   whseCode:string,
      /**  Controls if search results are consolidated into a single row when the only difference is Attribute Set ID.  */  
   consolidateInvAttributes:boolean,
}

export interface GetFullBinSearch_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
}

   /** Required : 
      @param partNum
      @param consolidateInvAttributes
      @param ds
   */  
export interface GetInventoryAttributeValuesOutDS_input{
   partNum:string,
   consolidateInvAttributes:boolean,
   ds:any,      //schema had no properties on an object.
}

export interface GetInventoryAttributeValuesOutDS_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataTableset:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param partNum
      @param consolidateInvAttributes
      @param ds
   */  
export interface GetInventoryAttributeValues_input{
   partNum:string,
   consolidateInvAttributes:boolean,
   ds:any,      //schema had no properties on an object.
}

export interface GetInventoryAttributeValues_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param partNum
      @param lotNum
      @param plant
      @param attributeSetID
   */  
export interface GetPartBinByLotAndPlant_input{
      /**  Part number  */  
   partNum:string,
      /**  Lot number - Optional  */  
   lotNum:string,
      /**  Plant - Optional  */  
   plant:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface GetPartBinByLotAndPlant_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
}

   /** Required : 
      @param partNum
      @param lotNum
      @param attributeSetID
   */  
export interface GetPartBinByLot_input{
      /**  Part number  */  
   partNum:string,
      /**  Lot number - Optional  */  
   lotNum:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface GetPartBinByLot_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
}

   /** Required : 
      @param pageSize
      @param absolutePage
      @param whereClause
   */  
export interface GetPartBinSearch_input{
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
      /**  Where Clause.  */  
   whereClause:string,
}

export interface GetPartBinSearch_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param partNum
      @param whseCode
      @param lotNum
      @param uomCode
      @param displayAllBins
      @param binNum
   */  
export interface GetSpecificBinSearch_input{
      /**  Part number. Required  */  
   partNum:string,
      /**  The Warehouse can be for a specific warehouse or null for all.  */  
   whseCode:string,
      /**  The Lot number can be for a specific lot if null is passed,
            only bins with no lot number will be returned.  */  
   lotNum:string,
      /**  The UOM Code can be for a specific Unit of Measure code if null is passed,
            only bins with no UOM codes will be returned.  */  
   uomCode:string,
      /**  True or False. False will search for bins with a qty ne 0.
            True will return all bins for a warehouse.  */  
   displayAllBins:boolean,
      /**  A specific Bin. Required.  */  
   binNum:string,
}

export interface GetSpecificBinSearch_output{
   returnObj:Erp_Tablesets_PartBinSearchTableset[],
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


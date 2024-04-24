import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MLSupplyDemandSvc
// Description: Material Supply Demand file.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/$metadata", {
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
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeSetIDFromRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/UpdateAttributeSetIDFromRevisionNum", {
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
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/PartsAttributeClassHasRevisionAndIsMRPTracked", {
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
   Summary: Invoke method GetSupplyDemand
   Description: This method returns the pegging information for the selected supply/demand/part.
No maintenance is allowed in this object so there is only this one method.
   OperationID: GetSupplyDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplyDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplyDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSupplyDemand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/GetSupplyDemand", {
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
export interface Erp_Tablesets_MLSupplyDemandTableset{
   PegRequest:Erp_Tablesets_PegRequestRow[],
   PegDemand:Erp_Tablesets_PegDemandRow[],
   PegDmdPart:Erp_Tablesets_PegDmdPartRow[],
   PegMtl:Erp_Tablesets_PegMtlRow[],
   PegSupply:Erp_Tablesets_PegSupplyRow[],
   PegDmdIndented:Erp_Tablesets_PegDmdIndentedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PegDemandRow{
   LinkID:number,
   Key1:string,
   Key2:string,
   Key3:string,
   Type:string,
   Quantity:number,
   PartNum:string,
   PartDesc:string,
   DueDate:string,
   SupplyDate:string,
   Warehouse:string,
   Plant:string,
      /**  The demand sequence number.  */  
   DmdSeq:number,
      /**  Sequence number of the Parent Demand  */  
   ParentDmd:number,
   SupplyType:string,
   SupKey1:string,
   SupKey2:string,
   SupKey3:string,
   DemandQty:number,
   AsmSeq:number,
   ParentAsm:number,
   JobReference:string,
   TOReference:string,
   SOReference:number,
   WhseReference:string,
   POReference:number,
      /**  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  */  
   TypeCode:string,
      /**  Contains the reference regardless of what type.  */  
   Reference:string,
      /**  Current Level  */  
   Level:number,
   ParentKey1:string,
   ParentKey2:string,
   ParentKey3:string,
   POSugReference:number,
   ConsumedQty:number,
      /**  Quantity UOM  */  
   QuantityUOM:string,
      /**  ConsumedQty UOM  */  
   ConsumedQtyUOM:string,
      /**  DemandQty UOM  */  
   DemandQtyUOM:string,
   LinkPart:string,
      /**  Plant Name  */  
   PlantName:string,
      /**  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  */  
   RowIdent:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  Description of values in set  */  
   DynAttrValueSetDescription:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PegDmdIndentedRow{
      /**  Current level  */  
   Level:number,
      /**  Part Number  */  
   PartNum:string,
      /**  Part Description  */  
   PartDesc:string,
      /**  Quantity Required  */  
   QtyRequired:number,
      /**  Manufactured, Purchased, or Transferred  */  
   MtlType:string,
      /**  Part Number prefixed by dots  */  
   PartNumIndented:string,
   Key1:string,
   Key2:string,
   Key3:string,
   ParentKey1:string,
   ParentKey2:string,
   ParentKey3:string,
   PeggedQty:number,
   SubAssy:boolean,
   ConsumedQty:number,
      /**  ConsumedQty UOM  */  
   ConsumedQtyUOM:string,
      /**  PeggedQty UOM  */  
   PeggedQtyUOM:string,
      /**  QtyRequired UOM  */  
   QtyRequiredUOM:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  Description of values in set  */  
   DynAttrValueSetDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PegDmdPartRow{
   LinkID:number,
      /**  Linked to the PegDemand.Key1  */  
   Key1:string,
      /**  Linked to the PegDemand.Key2  */  
   Key2:string,
      /**  Linked to the PegDemand.Key3  */  
   Key3:string,
   Type:string,
   Quantity:number,
   PartDesc:string,
   DueDate:string,
   SupplyDate:string,
   Warehouse:string,
   Plant:string,
   SeqNum:number,
   PartNum:string,
      /**  Sequence number of the associated Demand  */  
   DmdSeq:number,
      /**  Key field 1 of the Supply record.  */  
   SupKey1:string,
      /**  Key field 2 of the Supply record.  */  
   SupKey2:string,
      /**  Key field 3 of the Supply record.  */  
   SupKey3:string,
   DemandQty:number,
   JobReference:string,
   TOReference:string,
   SOReference:number,
   WhseReference:string,
   POReference:number,
      /**  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  */  
   TypeCode:string,
      /**  Contains the reference regardless of what type.  */  
   Reference:string,
      /**  Current Level  */  
   Level:number,
   POSugReference:number,
   ConsumedQty:number,
      /**  ConsumedQty UOM  */  
   ConsumedQtyUOM:string,
      /**  DemandQty UOM  */  
   DemandQtyUOM:string,
      /**  Quantity UOM  */  
   QuantityUOM:string,
      /**  Plant Name  */  
   PlantName:string,
      /**  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  */  
   RowIdent:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  Description of values in set  */  
   DynAttrValueSetDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PegMtlRow{
   LineNum:number,
   PartNum:string,
   PartDesc:string,
   Type:string,
   Quantity:number,
   DueDate:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Name:string,
   LinkID:number,
   SupKey1:string,
   SupKey2:string,
   SupKey3:string,
   DemandQty:number,
   JobReference:string,
   TOReference:string,
   SOReference:number,
   WhseReference:string,
   POReference:number,
      /**  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  */  
   TypeCode:string,
      /**  Contains the reference regardless of what type.  */  
   Reference:string,
   Warehouse:string,
   WhseRefDesc:string,
   POSugReference:number,
   ConsumedQty:number,
   PeggedQty:number,
      /**  ConsumedQty UOM  */  
   ConsumedQtyUOM:string,
      /**  DemandQty UOM  */  
   DemandQtyUOM:string,
      /**  PeggedQty UOM  */  
   PeggedQtyUOM:string,
      /**  Quantity UOM  */  
   QuantityUOM:string,
      /**  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  */  
   RowIdent:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  Description of values in set  */  
   DynAttrValueSetDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PegRequestRow{
   LinkID:number,
   Key1:string,
   Key2:string,
   Key3:string,
   Type:string,
   PartDesc:string,
   Quantity:number,
   PartNum:string,
   Reference:string,
   TypeCode:string,
      /**  Quantity UOM  */  
   QuantityUOM:string,
      /**  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  */  
   RowIdent:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  Description of values in set  */  
   DynAttrValueSetDescription:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PegSupplyRow{
   LinkID:number,
   Key1:string,
   Key2:string,
   Key3:string,
   Type:string,
   Quantity:number,
   PartNum:string,
   PartDesc:string,
   DueDate:string,
   DemandDate:string,
   Warehouse:string,
   Plant:string,
   JobReference:string,
   TOReference:string,
   SOReference:number,
   WhseReference:string,
   POReference:number,
      /**  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  */  
   TypeCode:string,
      /**  Contains the reference regardless of what type.  */  
   Reference:string,
   ParentKey1:string,
   ParentKey2:string,
   ParentKey3:string,
   POSugReference:number,
      /**  external field to the table that just indicates the sort order  */  
   TreeSort:number,
      /**  Quantity UOM  */  
   QuantityUOM:string,
      /**  Plant Name  */  
   PlantName:string,
      /**  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  */  
   RowIdent:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDescription:string,
      /**  The unique identifier of the Dynamic Attribute Set  */  
   DynAttrValueSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param key1
      @param key2
      @param key3
      @param key4
      @param mlType
      @param attributeSetID
   */  
export interface GetSupplyDemand_input{
      /**  First unique key  */  
   key1:string,
      /**  Second optional key  */  
   key2:string,
      /**  Third optional key  */  
   key3:string,
      /**  Third optional key  */  
   key4:string,
      /**  S = Sales Order, P = PO, J = Job, T = Transfer Order, R = Part  */  
   mlType:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface GetSupplyDemand_output{
   returnObj:Erp_Tablesets_MLSupplyDemandTableset[],
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

   /** Required : 
      @param attrClassID
   */  
export interface PartsAttributeClassHasRevisionAndIsMRPTracked_input{
      /**  current Attribute Class ID  */  
   attrClassID:string,
}

export interface PartsAttributeClassHasRevisionAndIsMRPTracked_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
      @param revisionNum
   */  
export interface UpdateAttributeSetIDFromRevisionNum_input{
      /**  current part number  */  
   partNum:string,
      /**  new revision selected  */  
   revisionNum:string,
}

export interface UpdateAttributeSetIDFromRevisionNum_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
   planningAttributeSetSeq:number,
}
}


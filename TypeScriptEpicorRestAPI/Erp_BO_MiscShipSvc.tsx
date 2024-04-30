import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MiscShipSvc
// Description: Miscellaneous Shipment Maintenance
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MiscShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MiscShips
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdRow
   */  
export function get_MiscShips(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MiscShips
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MscShpHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MiscShips(requestBody:Erp_Tablesets_MscShpHdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MiscShip item
   Description: Calls GetByID to retrieve the MiscShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MiscShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpHdRow
   */  
export function get_MiscShips_Company_PackNum(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpHdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")", {
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
         resolve(data as Erp_Tablesets_MscShpHdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MiscShip for the service
   Description: Calls UpdateExt to update MiscShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MiscShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MiscShips_Company_PackNum(Company:string, PackNum:string, requestBody:Erp_Tablesets_MscShpHdRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MiscShip item
   Description: Call UpdateExt to delete MiscShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MiscShip
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MiscShips_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get CartonTrkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CartonTrkDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_MiscShips_Company_PackNum_CartonTrkDtls(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/CartonTrkDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param CaseNum Desc: CaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_MiscShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, PackNum:string, ShipmentType:string, CaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
         resolve(data as Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MscShpDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpDts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtRow
   */  
export function get_MiscShips_Company_PackNum_MscShpDts(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpDts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpDt item
   Description: Calls GetByID to retrieve the MscShpDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpDtRow
   */  
export function get_MiscShips_Company_PackNum_MscShpDts_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")", {
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
         resolve(data as Erp_Tablesets_MscShpDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MscShpUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpUPS1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpUPSRow
   */  
export function get_MiscShips_Company_PackNum_MscShpUPS(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpUPS", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpUP item
   Description: Calls GetByID to retrieve the MscShpUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpUP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpUPSRow
   */  
export function get_MiscShips_Company_PackNum_MscShpUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MscShpHdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpHdAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdAttchRow
   */  
export function get_MiscShips_Company_PackNum_MscShpHdAttches(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpHdAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpHdAttch item
   Description: Calls GetByID to retrieve the MscShpHdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpHdAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   */  
export function get_MiscShips_Company_PackNum_MscShpHdAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpHdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpHdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CartonTrkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonTrkDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CartonTrkDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonTrkDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CartonTrkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonTrkDtls(requestBody:Erp_Tablesets_CartonTrkDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   */  
export function get_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonTrkDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
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
         resolve(data as Erp_Tablesets_CartonTrkDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CartonTrkDtl for the service
   Description: Calls UpdateExt to update CartonTrkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, requestBody:Erp_Tablesets_CartonTrkDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete CartonTrkDtl item
   Description: Call UpdateExt to delete CartonTrkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonTrkDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ShipmentType Desc: ShipmentType   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param CaseNum Desc: CaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company:string, ShipmentType:string, PackNum:string, CaseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MscShpDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpDts
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtRow
   */  
export function get_MscShpDts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpDts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MscShpDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MscShpDts(requestBody:Erp_Tablesets_MscShpDtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpDt item
   Description: Calls GetByID to retrieve the MscShpDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpDtRow
   */  
export function get_MscShpDts_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")", {
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
         resolve(data as Erp_Tablesets_MscShpDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MscShpDt for the service
   Description: Calls UpdateExt to update MscShpDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MscShpDts_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:Erp_Tablesets_MscShpDtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MscShpDt item
   Description: Call UpdateExt to delete MscShpDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpDt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MscShpDts_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get ShipCOOs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipCOOs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   */  
export function get_MscShpDts_Company_PackNum_PackLine_ShipCOOs(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ShipCOORow
   */  
export function get_MscShpDts_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, PackNum:string, PackLine:string, RelatedToFile:string, OrigCountry:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
         resolve(data as Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MscShpDtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpDtAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtAttchRow
   */  
export function get_MscShpDts_Company_PackNum_PackLine_MscShpDtAttches(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/MscShpDtAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpDtAttch item
   Description: Calls GetByID to retrieve the MscShpDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDtAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   */  
export function get_MscShpDts_Company_PackNum_PackLine_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ShipCOOs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipCOOs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   */  
export function get_ShipCOOs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipCOOs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ShipCOORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipCOOs(requestBody:Erp_Tablesets_ShipCOORow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ShipCOORow
   */  
export function get_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipCOORow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
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
         resolve(data as Erp_Tablesets_ShipCOORow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipCOO for the service
   Description: Calls UpdateExt to update ShipCOO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, requestBody:Erp_Tablesets_ShipCOORow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete ShipCOO item
   Description: Call UpdateExt to delete ShipCOO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipCOO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param OrigCountry Desc: OrigCountry   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company:string, RelatedToFile:string, PackNum:string, PackLine:string, OrigCountry:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MscShpDtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpDtAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtAttchRow
   */  
export function get_MscShpDtAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpDtAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MscShpDtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MscShpDtAttches(requestBody:Erp_Tablesets_MscShpDtAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpDtAttch item
   Description: Calls GetByID to retrieve the MscShpDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   */  
export function get_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpDtAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpDtAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MscShpDtAttch for the service
   Description: Calls UpdateExt to update MscShpDtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, requestBody:Erp_Tablesets_MscShpDtAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MscShpDtAttch item
   Description: Call UpdateExt to delete MscShpDtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpDtAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company:string, PackNum:string, PackLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MscShpUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpUPS
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpUPSRow
   */  
export function get_MscShpUPS(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpUPS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MscShpUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MscShpUPS(requestBody:Erp_Tablesets_MscShpUPSRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpUP item
   Description: Calls GetByID to retrieve the MscShpUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpUPSRow
   */  
export function get_MscShpUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MscShpUP for the service
   Description: Calls UpdateExt to update MscShpUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MscShpUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, requestBody:Erp_Tablesets_MscShpUPSRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MscShpUP item
   Description: Call UpdateExt to delete MscShpUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MscShpUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get MscShpHdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpHdAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdAttchRow
   */  
export function get_MscShpHdAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpHdAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MscShpHdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MscShpHdAttches(requestBody:Erp_Tablesets_MscShpHdAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MscShpHdAttch item
   Description: Calls GetByID to retrieve the MscShpHdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpHdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   */  
export function get_MscShpHdAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MscShpHdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MscShpHdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MscShpHdAttch for the service
   Description: Calls UpdateExt to update MscShpHdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpHdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MscShpHdAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_MscShpHdAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MscShpHdAttch item
   Description: Call UpdateExt to delete MscShpHdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpHdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MscShpHdAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMscShpHd:string, whereClauseMscShpHdAttch:string, whereClauseMscShpDt:string, whereClauseMscShpDtAttch:string, whereClauseShipCOO:string, whereClauseMscShpUPS:string, whereClauseCartonTrkDtl:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMscShpHd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMscShpHd=" + whereClauseMscShpHd
   }
   if(typeof whereClauseMscShpHdAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMscShpHdAttch=" + whereClauseMscShpHdAttch
   }
   if(typeof whereClauseMscShpDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMscShpDt=" + whereClauseMscShpDt
   }
   if(typeof whereClauseMscShpDtAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMscShpDtAttch=" + whereClauseMscShpDtAttch
   }
   if(typeof whereClauseShipCOO!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipCOO=" + whereClauseShipCOO
   }
   if(typeof whereClauseMscShpUPS!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMscShpUPS=" + whereClauseMscShpUPS
   }
   if(typeof whereClauseCartonTrkDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(packNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
   OperationID: AssignLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumber(requestBody:AssignLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/AssignLegalNumber", {
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
         resolve(data as AssignLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateWeight
   Description: calculate the weight of a carton based upon Part.Weight.
   OperationID: CalculateWeight
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateWeight(requestBody:CalculateWeight_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateWeight_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CalculateWeight", {
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
         resolve(data as CalculateWeight_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelVoidCarton
   Description: Checks to see if the carton void can be cancelled and re-opens it if it is allowed.
   OperationID: CancelVoidCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CancelVoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelVoidCarton(requestBody:CancelVoidCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CancelVoidCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CancelVoidCarton", {
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
         resolve(data as CancelVoidCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCOOPercents
   Description: Checks to see if the Qty percent and value percent fields total 100 percent.
   OperationID: CheckCOOPercents
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCOOPercents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOOPercents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOOPercents(requestBody:CheckCOOPercents_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCOOPercents_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CheckCOOPercents", {
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
         resolve(data as CheckCOOPercents_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearConvertedManifest
   Description: Clear MscShpHd Manifest fields when Unfreighting.
   OperationID: ClearConvertedManifest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearConvertedManifest(requestBody:ClearConvertedManifest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearConvertedManifest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ClearConvertedManifest", {
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
         resolve(data as ClearConvertedManifest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseCarton
   Description: Checks to see if the carton can be closed and closes it if it is allowed.
   OperationID: CloseCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseCarton(requestBody:CloseCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CloseCarton", {
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
         resolve(data as CloseCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConvertToManifestUOM
   Description: Populate MscShpHd Manifest fields.
   OperationID: ConvertToManifestUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertToManifestUOM(requestBody:ConvertToManifestUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConvertToManifestUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ConvertToManifestUOM", {
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
         resolve(data as ConvertToManifestUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMiscShipRecsFromDMR
   Description: Creates Miscellaneous Shipment Records from DRM Entries. Header and details.
   OperationID: CreateMiscShipRecsFromDMR
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMiscShipRecsFromDMR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMiscShipRecsFromDMR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMiscShipRecsFromDMR(requestBody:CreateMiscShipRecsFromDMR_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMiscShipRecsFromDMR_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CreateMiscShipRecsFromDMR", {
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
         resolve(data as CreateMiscShipRecsFromDMR_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CallsCreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipPackNum">Current packNum</param><param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:  Called from Kinetic so first need to dirty rows
   OperationID: CallsCreateCustomerCartons
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CallsCreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CallsCreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CallsCreateCustomerCartons(requestBody:CallsCreateCustomerCartons_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CallsCreateCustomerCartons_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CallsCreateCustomerCartons", {
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
         resolve(data as CallsCreateCustomerCartons_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:
   OperationID: CreateCustomerCartons
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateCustomerCartons(requestBody:CreateCustomerCartons_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateCustomerCartons_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CreateCustomerCartons", {
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
         resolve(data as CreateCustomerCartons_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CartonValidateWeight
   Description: Purpose:
<param name="ipWeight"> weight to validate</param>
Notes:
   OperationID: CartonValidateWeight
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CartonValidateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonValidateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonValidateWeight(requestBody:CartonValidateWeight_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CartonValidateWeight_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonValidateWeight", {
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
         resolve(data as CartonValidateWeight_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckValidCartonWeight
   Description: Purpose: Ensure the carton weight is valid.
<param name="ipPackNum">Pack Num to validate weights</param>
Notes:
   OperationID: CheckValidCartonWeight
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckValidCartonWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidCartonWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckValidCartonWeight(requestBody:CheckValidCartonWeight_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckValidCartonWeight_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CheckValidCartonWeight", {
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
         resolve(data as CheckValidCartonWeight_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCartonPackaging
   Description: Purpose: Obtain the carton package specs
<param name="ipPkgCode">package code</param><param name="opPkgHeight">package height</param><param name="opPkgWidth">package width</param><param name="opPkgLength">package length</param>
Notes:
   OperationID: GetCartonPackaging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCartonPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCartonPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCartonPackaging(requestBody:GetCartonPackaging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCartonPackaging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetCartonPackaging", {
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
         resolve(data as GetCartonPackaging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackWeightWithCarton
   Description: Purpose:Update the Pack Weight with the carton weight
<param name="ipPackNum">Pack Number to process</param><param name="ipOldWeight">Previous weight</param><param name="ipWeight">Current Case weight</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackWeightWithCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePackWeightWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackWeightWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackWeightWithCarton(requestBody:UpdatePackWeightWithCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePackWeightWithCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/UpdatePackWeightWithCarton", {
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
         resolve(data as UpdatePackWeightWithCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackCODWithCarton
   Description: Purpose: Update pack COD amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero</param><param name="ipOldCOD">Previous COD</param><param name="ipCOD">Current Case COD</param><param name="ipFlag">Current COD flag value</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackCODWithCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePackCODWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackCODWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackCODWithCarton(requestBody:UpdatePackCODWithCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePackCODWithCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/UpdatePackCODWithCarton", {
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
         resolve(data as UpdatePackCODWithCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePackDeclaredWithCarton
   Description: Purpose:  Update Pack Delcared Value Amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero </param><param name="ipOldDeclared">Previous COD</param><param name="ipDeclared">Current Case COD</param><param name="ipDeclaredFlag">current setting of declared insurance</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackDeclaredWithCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdatePackDeclaredWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackDeclaredWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePackDeclaredWithCarton(requestBody:UpdatePackDeclaredWithCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdatePackDeclaredWithCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/UpdatePackDeclaredWithCarton", {
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
         resolve(data as UpdatePackDeclaredWithCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeletePhantomPacks
   Description: Purpose:
<param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeletePhantomPacks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeletePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePhantomPacks(requestBody:DeletePhantomPacks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeletePhantomPacks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/DeletePhantomPacks", {
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
         resolve(data as DeletePhantomPacks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRangePhantomPacks
   Description: Purpose:
<param name="ipFromCase">First case number to start deletes</param><param name="ipToCase">Last case number to delete</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeleteRangePhantomPacks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRangePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRangePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRangePhantomPacks(requestBody:DeleteRangePhantomPacks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRangePhantomPacks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/DeleteRangePhantomPacks", {
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
         resolve(data as DeleteRangePhantomPacks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAddrInfo
   Description: This method updates the address information from either the Vendor or Customer
table when the Shipto or PurPoint field has been changed.  If custID and VendorID fields are
both blank this procedure assumes that the user is entering the information in free form and
there is nothing to default (or no need to call this method).
   OperationID: GetAddrInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAddrInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAddrInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAddrInfo(requestBody:GetAddrInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAddrInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetAddrInfo", {
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
         resolve(data as GetAddrInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCallInfo
   Description: This method defaults the Call Number and shipto fields when the Job, PO or Order
number fields change
   OperationID: GetCallInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCallInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCallInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCallInfo(requestBody:GetCallInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCallInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetCallInfo", {
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
         resolve(data as GetCallInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultUOM
   Description: Gets the default UOM from Part or XaSyst
   OperationID: GetDefaultUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultUOM(requestBody:GetDefaultUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetDefaultUOM", {
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
         resolve(data as GetDefaultUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDMRSupplierInfo
   Description: Gets DRM Supplier's info
   OperationID: GetDMRSupplierInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDMRSupplierInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDMRSupplierInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDMRSupplierInfo(requestBody:GetDMRSupplierInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDMRSupplierInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetDMRSupplierInfo", {
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
         resolve(data as GetDMRSupplierInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:GetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetLegalNumGenOpts", {
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
         resolve(data as GetLegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMtlInfo
   Description: This method defaults the Quantity, Part and Line description fields
when the MtlSeq field has been updated
   OperationID: GetMtlInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlInfo(requestBody:GetMtlInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMtlInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetMtlInfo", {
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
         resolve(data as GetMtlInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackageClass
   OperationID: GetPackageClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackageClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageClass(requestBody:GetPackageClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackageClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetPackageClass", {
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
         resolve(data as GetPackageClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of PartNum changes.
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangingAttributeSet", {
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
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangingRevisionNum", {
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
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuantity
   Description: Call this method when the value of Quantity changes.
   OperationID: OnChangeQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuantity(requestBody:OnChangeQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangeQuantity", {
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
         resolve(data as OnChangeQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeIUM
   Description: Call this method when the value of IUM changes.
   OperationID: OnChangeIUM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIUM(requestBody:OnChangeIUM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeIUM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OnChangeIUM", {
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
         resolve(data as OnChangeIUM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackaging
   OperationID: GetPackaging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackaging(requestBody:GetPackaging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackaging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetPackaging", {
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
         resolve(data as GetPackaging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOSupplierInfo
   Description: Gets PO Supplier's info
   OperationID: GetPOSupplierInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPOSupplierInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOSupplierInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOSupplierInfo(requestBody:GetPOSupplierInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOSupplierInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetPOSupplierInfo", {
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
         resolve(data as GetPOSupplierInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetScale
   Description: none
   OperationID: GetScale
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetScale(requestBody:GetScale_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetScale_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetScale", {
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
         resolve(data as GetScale_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranDocTypeID(requestBody:GetTranDocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetTranDocTypeID", {
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
         resolve(data as GetTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRMACustomerInfo
   Description: Gets RMA Ship to's info
   OperationID: GetRMACustomerInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRMACustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMACustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRMACustomerInfo(requestBody:GetRMACustomerInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRMACustomerInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetRMACustomerInfo", {
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
         resolve(data as GetRMACustomerInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OpenCarton
   Description: Checks to see if the carton can be opened and opens it if it is allowed.
   OperationID: OpenCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OpenCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenCarton(requestBody:OpenCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OpenCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/OpenCarton", {
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
         resolve(data as OpenCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrintSlip
   Description: This method prints the Miscellaneous Packing Slip
   OperationID: PrintSlip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrintSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintSlip(requestBody:PrintSlip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrintSlip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/PrintSlip", {
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
         resolve(data as PrintSlip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVEnable
   OperationID: SetUPSQVEnable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVEnable(requestBody:SetUPSQVEnable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetUPSQVEnable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/SetUPSQVEnable", {
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
         resolve(data as SetUPSQVEnable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVShipStatus
   OperationID: SetUPSQVShipStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVShipStatus(requestBody:SetUPSQVShipStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetUPSQVShipStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/SetUPSQVShipStatus", {
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
         resolve(data as SetUPSQVShipStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrigCountry
   Description: Method to change related fields to the country. Run when the country changes.
   OperationID: ChangeOrigCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrigCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrigCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrigCountry(requestBody:ChangeOrigCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrigCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ChangeOrigCountry", {
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
         resolve(data as ChangeOrigCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StageCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: StageCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/StageCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StageCarton(requestBody:StageCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<StageCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/StageCarton", {
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
         resolve(data as StageCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Calculate the CODAmount and DeclaredAmt
   OperationID: UpdateManifestChargeAmts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateManifestChargeAmts(requestBody:UpdateManifestChargeAmts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateManifestChargeAmts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/UpdateManifestChargeAmts", {
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
         resolve(data as UpdateManifestChargeAmts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: VoidCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidCarton(requestBody:VoidCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/VoidCarton", {
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
         resolve(data as VoidCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:VoidLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/VoidLegalNumber", {
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
         resolve(data as VoidLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateDigitalSignature(requestBody:GenerateDigitalSignature_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateDigitalSignature_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GenerateDigitalSignature", {
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
         resolve(data as GenerateDigitalSignature_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: none
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: none
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllowsDecimals
   Description: Checks if the current UOM class allows decimals
   OperationID: GetAllowsDecimals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllowsDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllowsDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllowsDecimals(requestBody:GetAllowsDecimals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllowsDecimals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetAllowsDecimals", {
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
         resolve(data as GetAllowsDecimals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateShipmentFromWIP
   Description: Creates a shipment from a Job with a make to stock demand link marked as Misc Shipment from WIP
   OperationID: CreateShipmentFromWIP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateShipmentFromWIP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateShipmentFromWIP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateShipmentFromWIP(requestBody:CreateShipmentFromWIP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateShipmentFromWIP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CreateShipmentFromWIP", {
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
         resolve(data as CreateShipmentFromWIP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMscShpHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMscShpHd(requestBody:GetNewMscShpHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMscShpHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewMscShpHd", {
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
         resolve(data as GetNewMscShpHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMscShpHdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpHdAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMscShpHdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpHdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMscShpHdAttch(requestBody:GetNewMscShpHdAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMscShpHdAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewMscShpHdAttch", {
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
         resolve(data as GetNewMscShpHdAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMscShpDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpDt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMscShpDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMscShpDt(requestBody:GetNewMscShpDt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMscShpDt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewMscShpDt", {
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
         resolve(data as GetNewMscShpDt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMscShpDtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpDtAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMscShpDtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpDtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMscShpDtAttch(requestBody:GetNewMscShpDtAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMscShpDtAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewMscShpDtAttch", {
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
         resolve(data as GetNewMscShpDtAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewShipCOO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipCOO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewShipCOO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipCOO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipCOO(requestBody:GetNewShipCOO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewShipCOO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewShipCOO", {
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
         resolve(data as GetNewShipCOO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMscShpUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpUPS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMscShpUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMscShpUPS(requestBody:GetNewMscShpUPS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMscShpUPS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewMscShpUPS", {
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
         resolve(data as GetNewMscShpUPS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCartonTrkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCartonTrkDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCartonTrkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCartonTrkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCartonTrkDtl(requestBody:GetNewCartonTrkDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCartonTrkDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetNewCartonTrkDtl", {
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
         resolve(data as GetNewCartonTrkDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CartonTrkDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpDtAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpDtRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpHdAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpHdListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpHdRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MscShpUPSRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipCOORow,
}

export interface Erp_Tablesets_CartonTrkDtlRow{
      /**  Company ID  */  
   "Company":string,
      /**  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  */  
   "ShipmentType":string,
      /**  The pack number associated with the tracking number.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  */  
   "CaseNum":number,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  Package Weight  */  
   "PkgWeight":number,
      /**  Prefer COD delivery.  Reserved for future development.  */  
   "CODFlag":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order.  Reserved for future development.  */  
   "CODAmount":number,
      /**  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  */  
   "DeclaredValueFlag":boolean,
      /**  Declared Insurance Amount.  Reserved for future development.  */  
   "DeclaredValue":number,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Collect On Delivery Value  */  
   "CODValue":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Concatenated field consisting of PackNum and CaseNum separated by a dash.  */  
   "CaseID":string,
      /**  Status of the shipment.  */  
   "PackStatus":string,
      /**  logical used by UI for row rules  */  
   "PhantomPack":boolean,
   "CapturePt":string,
      /**  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  */  
   "EnablePhantom":boolean,
   "KitPartAttrClassID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpDtAttchRow{
   "Company":string,
   "PackNum":number,
   "PackLine":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpDtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Number of Packages.  */  
   "Packages":number,
      /**  Part number of item actually shipped.  */  
   "PartNum":string,
      /**  Line description.  */  
   "LineDesc":string,
      /**  Unit of measure  */  
   "IUM":string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   "RevisionNum":string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   "XRevisionNum":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   "ShpConNum":number,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   "WUM":string,
      /**  Lot Number is defaulted as Job Number.  */  
   "LotNum":string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   "CustNum":number,
      /**  The shipto number. Used for warranty validation.  */  
   "ShipToNum":string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   "Plant":string,
      /**  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  */  
   "Quantity":number,
      /**  The Service Call number that this Job is related to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is related to.  */  
   "CallLine":number,
      /**  The JobMtl seq that this record relates to.  */  
   "MtlSeq":number,
      /**  Assembly sequence number that this shipment is associated with.  */  
   "AssemblySeq":number,
      /**  Job number.  This is the job that the service call line is linke to.  */  
   "JobNum":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Related RMA Receipt  */  
   "RMAReceipt":number,
      /**  Related RMA Disposition  */  
   "RMADisp":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Determines if the Shipment has to be synchronized with Epicor FSA application.  */  
   "EpicorFSA":boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   "FSAInstallationPrice":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   "FSAInstallationType":string,
   "FSAInstallationTypeDescription":string,
      /**  Indicates if the shipment requires to create an Equipment Delivery Performed line on the resulting FSA Service Order in Epicor FSA.  */  
   "FSARequiresServiceOrder":boolean,
   "PartAESExp":string,
      /**  Used by freighting web service  */  
   "PartEcnNumber":string,
      /**  Used by freighting web service  */  
   "PartExpLicNumber":string,
      /**  Used by freighting web service  */  
   "PartExpLicType":string,
      /**  Used by freighting web service  */  
   "PartHazClass":string,
      /**  Used by freighting web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by freighting web service  */  
   "PartHazItem":boolean,
      /**  Used by freighting web service  */  
   "PartHazPackInstr":string,
   "PartHazSub":string,
   "PartHazTechName":string,
      /**  Used by freighting web service  */  
   "PartHTS":string,
      /**  Used by freighting web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by freighting web service  */  
   "PartNAFTAPref":string,
      /**  Used by freighting web service  */  
   "PartNAFTAProd":string,
      /**  Used by freighting web service  */  
   "PartOrigCountry":string,
   "PartSchedBCode":string,
   "PartUseHTSDesc":boolean,
      /**  Indicates if the Job is a Service Call  */  
   "ServiceJob":boolean,
      /**  ship status of the MscShpHd  */  
   "ShipStatus":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "CallLineLineDesc":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "JobNumPartDescription":string,
   "MtlSeqSalvageDescription":string,
   "MtlSeqDescription":string,
   "PackNumName":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumAttrClassID":string,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpHdAttchRow{
   "Company":string,
   "PackNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpHdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  */  
   "OrderNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "Name":string,
      /**  The first line of the main address.  */  
   "Address1":string,
      /**  The second line of the main address.  */  
   "Address2":string,
      /**  The third line of the main address.  */  
   "Address3":string,
      /**  The city portion of the shipping  address.  */  
   "City":string,
      /**  State ID for the ShipTo.  Can be blank.  */  
   "State":string,
      /**  The zip or postal code portion of the shipping  address.  */  
   "ZIP":string,
      /**  The country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  */  
   "FaxNum":string,
      /**  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  */  
   "PurPoint":string,
      /**  A  unique integer to identify vendors.  */  
   "VendorNum":number,
      /**  The Service Call number that this Job is related to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is related to.  */  
   "CallLine":number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Packaging code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling Required flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Package flag.  */  
   "NonStdPkg":boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   "FFCountryNum":number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress3":string,
      /**  Shipping, The country number of the Payer main address.  */  
   "PayBTCountryNum":number,
      /**  Shipping, The phone number of the Payer main address.  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantity View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantity View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantity View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if Customer is on credit Hold  */  
   "OnCreditHold":boolean,
      /**  Job Type Description  */  
   "JobType":string,
      /**  List delimited Address fields using the Address Format rules  */  
   "AddrList":string,
   "ShipStatusDescription":string,
      /**  Carton Stage number  */  
   "CartonStageNbr":string,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton width  */  
   "CartonWidth":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  The sum of the vlaue of items in the carton.  */  
   "CartonContentValue":number,
      /**  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   "PkgLenEnable":number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   "PkgWidthEnable":number,
      /**  A zero indicates the Packing height is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  logical indicating if the weight prompt is enabled.  */  
   "EnableWeight":boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   "MasterpackPackNum":number,
   "PkgSizeUOMEnable":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if TranDocTypeID is available for input  */  
   "EnableTranDocType":boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  Country name  */  
   "CountryNumDescription":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  State portion of the address  */  
   "PurPointState":string,
      /**  Third address line  */  
   "PurPointAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "PurPointName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "PurPointZip":string,
      /**  First address line  */  
   "PurPointAddress1":string,
      /**  City portion of the address  */  
   "PurPointCity":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PurPointPrimPCon":number,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "vrPONumShipToConName":string,
      /**  defaults from the company file.  */  
   "vrPONumShipName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpHdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  */  
   "OrderNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "Name":string,
      /**  The first line of the main address.  */  
   "Address1":string,
      /**  The second line of the main address.  */  
   "Address2":string,
      /**  The third line of the main address.  */  
   "Address3":string,
      /**  The city portion of the shipping  address.  */  
   "City":string,
      /**  State ID for the ShipTo.  Can be blank.  */  
   "State":string,
      /**  The zip or postal code portion of the shipping  address.  */  
   "ZIP":string,
      /**  The country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  */  
   "FaxNum":string,
      /**  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  */  
   "PurPoint":string,
      /**  A  unique integer to identify vendors.  */  
   "VendorNum":number,
      /**  The Service Call number that this Job is related to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is related to.  */  
   "CallLine":number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Packaging code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling Required flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Package flag.  */  
   "NonStdPkg":boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   "FFCountryNum":number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress3":string,
      /**  Shipping, The country number of the Payer main address.  */  
   "PayBTCountryNum":number,
      /**  Shipping, The phone number of the Payer main address.  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantity View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantity View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantity View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAuthorizationCode  */  
   "AGAuthorizationCode":string,
      /**  AGAuthorizationDate  */  
   "AGAuthorizationDate":string,
      /**  AGCarrierCUIT  */  
   "AGCarrierCUIT":string,
      /**  AGDocumentLetter  */  
   "AGDocumentLetter":string,
      /**  AGInvoicingPoint  */  
   "AGInvoicingPoint":string,
      /**  AGLegalNumber  */  
   "AGLegalNumber":string,
      /**  AGPrintingControlType  */  
   "AGPrintingControlType":string,
      /**  AGTrackLicense  */  
   "AGTrackLicense":string,
      /**  AGShippingWay  */  
   "AGShippingWay":string,
      /**  Indicates if the Miscellaneous Shipment is a DMR Pack  */  
   "IsDMRPack":boolean,
      /**  Dispatch Reason Code used for Customer Shipment  */  
   "DispatchReason":string,
      /**  AGCOTMark  */  
   "AGCOTMark":boolean,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  DigitalSignature  */  
   "DigitalSignature":string,
      /**  SignedOn  */  
   "SignedOn":string,
      /**  SignedBy  */  
   "SignedBy":string,
      /**  FirstPrintDate  */  
   "FirstPrintDate":string,
      /**  DocCopyNum  */  
   "DocCopyNum":number,
      /**  EpicorFSA  */  
   "EpicorFSA":boolean,
      /**  RMA Number linked to the Miscellaneous Shipment.  */  
   "RMANum":number,
      /**  RMA Line linked to the Miscellaneous Shipment.  */  
   "RMALine":number,
      /**  True if ready to send to FSA  */  
   "FSAReady":boolean,
      /**  True if created as return shipment from RMA or DMR or Job  */  
   "FromDepotRepair":boolean,
      /**  True if MscShpHd was created from Job Closing for Misc Shipment to WIP functionality.  */  
   "FromJobClosing":boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  The sum of the vlaue of items in the carton.  */  
   "CartonContentValue":number,
      /**  Carton Height  */  
   "CartonHeight":number,
      /**  Carton length  */  
   "CartonLength":number,
      /**  Carton Stage number  */  
   "CartonStageNbr":string,
      /**  Carton width  */  
   "CartonWidth":number,
   "DspDigitalSignature":string,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  logical indicating if the weight prompt is enabled.  */  
   "EnableWeight":boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Job Type Description  */  
   "JobType":string,
      /**  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  */  
   "LastCartonFlag":boolean,
   "LegalNumberMessage":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   "MasterpackPackNum":number,
      /**  Indicates if Customer is on credit Hold  */  
   "OnCreditHold":boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   "PkgLenEnable":number,
   "PkgSizeUOMEnable":number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   "PkgWidthEnable":number,
   "ShipStatusDescription":string,
      /**  List delimited Address fields using the Address Format rules  */  
   "AddrList":string,
   "QSUseBOL":boolean,
   "QSUseIntl":boolean,
   "QSUseCO":boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   "EnablePhantom":boolean,
      /**  Logical indicating if CartonTrkDtl records exist for this pack. Used by the UI for row rules.  */  
   "PhantomCasesExist":boolean,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "CallLineLineDesc":string,
   "CountryNumDescription":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "DeliveryTypeDescription":string,
   "FreightedShipViaCodeWebDesc":string,
   "FreightedShipViaCodeDescription":string,
   "JobNumPartDescription":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "PurPointPrimPCon":number,
   "PurPointName":string,
   "PurPointState":string,
   "PurPointCity":string,
   "PurPointAddress3":string,
   "PurPointAddress2":string,
   "PurPointCountry":string,
   "PurPointAddress1":string,
   "PurPointZip":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TranDocTypeDescription":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
   "VendorNumCity":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "vrPONumShipToConName":string,
   "vrPONumShipName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MscShpUPSRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  UPS Quantity View Sequence  */  
   "UPSQVSeq":number,
      /**  Email adress to be used for notifications.  */  
   "EmailAddress":string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if the UPS quantum view is to be enabled.  */  
   "EnableQuantumView":boolean,
   "ShipStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipCOORow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  CountryNum for Country of Origin  */  
   "OrigCountry":number,
      /**  Qty percent of this part which is from this country of origin.  */  
   "QtyPerc":number,
      /**  Value percent of this part from this country of origin.  */  
   "ValuePerc":number,
      /**  Is this the primary country of origin for this part  */  
   "Primary":boolean,
      /**  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  */  
   "RelatedToFile":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param cartonNumber
   */  
export interface CalculateWeight_input{
      /**  Carton Number  */  
   cartonNumber:number,
}

export interface CalculateWeight_output{
parameters : {
      /**  output parameters  */  
   calculatedWeight:number,
}
}

   /** Required : 
      @param ipPackNum
      @param ipNbrCartonsToCreate
      @param ipPkgCode
      @param ipPkgLength
      @param ipPkgWidth
      @param ipPkgHeight
      @param ipRecalcAmts
      @param ipZeroWeight
      @param ds
   */  
export interface CallsCreateCustomerCartons_input{
   ipPackNum:number,
   ipNbrCartonsToCreate:number,
   ipPkgCode:string,
   ipPkgLength:number,
   ipPkgWidth:number,
   ipPkgHeight:number,
   ipRecalcAmts:boolean,
   ipZeroWeight:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface CallsCreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param iPackNum
   */  
export interface CancelVoidCarton_input{
      /**  The carton number of the carton to open  */  
   iPackNum:number,
}

export interface CancelVoidCarton_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param ipWeight
   */  
export interface CartonValidateWeight_input{
   ipWeight:number,
}

export interface CartonValidateWeight_output{
}

   /** Required : 
      @param i_CountryNum
   */  
export interface ChangeOrigCountry_input{
      /**  Country Number  */  
   i_CountryNum:number,
}

export interface ChangeOrigCountry_output{
}

   /** Required : 
      @param iPackNum
      @param iPackLine
   */  
export interface CheckCOOPercents_input{
      /**  The current PackNum  */  
   iPackNum:number,
      /**  The current PackLine  */  
   iPackLine:number,
}

export interface CheckCOOPercents_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface CheckValidCartonWeight_input{
   ipPackNum:number,
}

export interface CheckValidCartonWeight_output{
}

   /** Required : 
      @param ipPackNum
   */  
export interface ClearConvertedManifest_input{
      /**  Pack Num to clear Manifest fields  */  
   ipPackNum:number,
}

export interface ClearConvertedManifest_output{
}

   /** Required : 
      @param iPackNum
      @param ds
   */  
export interface CloseCarton_input{
      /**  The carton number of the carton to close  */  
   iPackNum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface CloseCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface ConvertToManifestUOM_input{
      /**  Pack Num to populate Manifest fields  */  
   ipPackNum:number,
}

export interface ConvertToManifestUOM_output{
}

   /** Required : 
      @param ipNbrCartonsToCreate
      @param ipPkgCode
      @param ipPkgLength
      @param ipPkgWidth
      @param ipPkgHeight
      @param ipRecalcAmts
      @param ipZeroWeight
      @param ds
   */  
export interface CreateCustomerCartons_input{
   ipNbrCartonsToCreate:number,
   ipPkgCode:string,
   ipPkgLength:number,
   ipPkgWidth:number,
   ipPkgHeight:number,
   ipRecalcAmts:boolean,
   ipZeroWeight:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface CreateCustomerCartons_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipDMRNum
   */  
export interface CreateMiscShipRecsFromDMR_input{
      /**  DMR number supplied  */  
   ipDMRNum:number,
}

export interface CreateMiscShipRecsFromDMR_output{
}

   /** Required : 
      @param jobNum
   */  
export interface CreateShipmentFromWIP_input{
   jobNum:string,
}

export interface CreateShipmentFromWIP_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param packNum
   */  
export interface DeleteByID_input{
   packNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeletePhantomPacks_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface DeletePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipFromCase
      @param ipToCase
      @param ds
   */  
export interface DeleteRangePhantomPacks_input{
   ipFromCase:number,
   ipToCase:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface DeleteRangePhantomPacks_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

export interface Erp_Tablesets_CartonTrkDtlRow{
      /**  Company ID  */  
   Company:string,
      /**  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  */  
   ShipmentType:string,
      /**  The pack number associated with the tracking number.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  */  
   CaseNum:number,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  Package Weight  */  
   PkgWeight:number,
      /**  Prefer COD delivery.  Reserved for future development.  */  
   CODFlag:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order.  Reserved for future development.  */  
   CODAmount:number,
      /**  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  */  
   DeclaredValueFlag:boolean,
      /**  Declared Insurance Amount.  Reserved for future development.  */  
   DeclaredValue:number,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Collect On Delivery Value  */  
   CODValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Concatenated field consisting of PackNum and CaseNum separated by a dash.  */  
   CaseID:string,
      /**  Status of the shipment.  */  
   PackStatus:string,
      /**  logical used by UI for row rules  */  
   PhantomPack:boolean,
   CapturePt:string,
      /**  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  */  
   EnablePhantom:boolean,
   KitPartAttrClassID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_MiscShipTableset{
   MscShpHd:Erp_Tablesets_MscShpHdRow[],
   MscShpHdAttch:Erp_Tablesets_MscShpHdAttchRow[],
   MscShpDt:Erp_Tablesets_MscShpDtRow[],
   MscShpDtAttch:Erp_Tablesets_MscShpDtAttchRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   MscShpUPS:Erp_Tablesets_MscShpUPSRow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MscShpDtAttchRow{
   Company:string,
   PackNum:number,
   PackLine:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MscShpDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Number of Packages.  */  
   Packages:number,
      /**  Part number of item actually shipped.  */  
   PartNum:string,
      /**  Line description.  */  
   LineDesc:string,
      /**  Unit of measure  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   XRevisionNum:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   ShpConNum:number,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   WUM:string,
      /**  Lot Number is defaulted as Job Number.  */  
   LotNum:string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   CustNum:number,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  */  
   Quantity:number,
      /**  The Service Call number that this Job is related to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is related to.  */  
   CallLine:number,
      /**  The JobMtl seq that this record relates to.  */  
   MtlSeq:number,
      /**  Assembly sequence number that this shipment is associated with.  */  
   AssemblySeq:number,
      /**  Job number.  This is the job that the service call line is linke to.  */  
   JobNum:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Related RMA Receipt  */  
   RMAReceipt:number,
      /**  Related RMA Disposition  */  
   RMADisp:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Determines if the Shipment has to be synchronized with Epicor FSA application.  */  
   EpicorFSA:boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   FSAInstallationPrice:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   FSAInstallationType:string,
   FSAInstallationTypeDescription:string,
      /**  Indicates if the shipment requires to create an Equipment Delivery Performed line on the resulting FSA Service Order in Epicor FSA.  */  
   FSARequiresServiceOrder:boolean,
   PartAESExp:string,
      /**  Used by freighting web service  */  
   PartEcnNumber:string,
      /**  Used by freighting web service  */  
   PartExpLicNumber:string,
      /**  Used by freighting web service  */  
   PartExpLicType:string,
      /**  Used by freighting web service  */  
   PartHazClass:string,
      /**  Used by freighting web service  */  
   PartHazGvrnmtID:string,
      /**  Used by freighting web service  */  
   PartHazItem:boolean,
      /**  Used by freighting web service  */  
   PartHazPackInstr:string,
   PartHazSub:string,
   PartHazTechName:string,
      /**  Used by freighting web service  */  
   PartHTS:string,
      /**  Used by freighting web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by freighting web service  */  
   PartNAFTAPref:string,
      /**  Used by freighting web service  */  
   PartNAFTAProd:string,
      /**  Used by freighting web service  */  
   PartOrigCountry:string,
   PartSchedBCode:string,
   PartUseHTSDesc:boolean,
      /**  Indicates if the Job is a Service Call  */  
   ServiceJob:boolean,
      /**  ship status of the MscShpHd  */  
   ShipStatus:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   JobNumPartDescription:string,
   MtlSeqSalvageDescription:string,
   MtlSeqDescription:string,
   PackNumName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumAttrClassID:string,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MscShpHdAttchRow{
   Company:string,
   PackNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MscShpHdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  */  
   OrderNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   Name:string,
      /**  The first line of the main address.  */  
   Address1:string,
      /**  The second line of the main address.  */  
   Address2:string,
      /**  The third line of the main address.  */  
   Address3:string,
      /**  The city portion of the shipping  address.  */  
   City:string,
      /**  State ID for the ShipTo.  Can be blank.  */  
   State:string,
      /**  The zip or postal code portion of the shipping  address.  */  
   ZIP:string,
      /**  The country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  */  
   FaxNum:string,
      /**  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  */  
   PurPoint:string,
      /**  A  unique integer to identify vendors.  */  
   VendorNum:number,
      /**  The Service Call number that this Job is related to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is related to.  */  
   CallLine:number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Packaging code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   FFCountryNum:number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress3:string,
      /**  Shipping, The country number of the Payer main address.  */  
   PayBTCountryNum:number,
      /**  Shipping, The phone number of the Payer main address.  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantity View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if Customer is on credit Hold  */  
   OnCreditHold:boolean,
      /**  Job Type Description  */  
   JobType:string,
      /**  List delimited Address fields using the Address Format rules  */  
   AddrList:string,
   ShipStatusDescription:string,
      /**  Carton Stage number  */  
   CartonStageNbr:string,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton width  */  
   CartonWidth:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  The sum of the vlaue of items in the carton.  */  
   CartonContentValue:number,
      /**  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   PkgLenEnable:number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   PkgWidthEnable:number,
      /**  A zero indicates the Packing height is to be enabled.  */  
   PkgHeightEnable:number,
      /**  logical indicating if the weight prompt is enabled.  */  
   EnableWeight:boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   MasterpackPackNum:number,
   PkgSizeUOMEnable:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if TranDocTypeID is available for input  */  
   EnableTranDocType:boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  Country name  */  
   CountryNumDescription:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  State portion of the address  */  
   PurPointState:string,
      /**  Third address line  */  
   PurPointAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   PurPointName:string,
      /**  Postal Code or Zip code portion of the address  */  
   PurPointZip:string,
      /**  First address line  */  
   PurPointAddress1:string,
      /**  City portion of the address  */  
   PurPointCity:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PurPointPrimPCon:number,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   vrPONumShipToConName:string,
      /**  defaults from the company file.  */  
   vrPONumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MscShpHdListTableset{
   MscShpHdList:Erp_Tablesets_MscShpHdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MscShpHdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  */  
   OrderNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   Name:string,
      /**  The first line of the main address.  */  
   Address1:string,
      /**  The second line of the main address.  */  
   Address2:string,
      /**  The third line of the main address.  */  
   Address3:string,
      /**  The city portion of the shipping  address.  */  
   City:string,
      /**  State ID for the ShipTo.  Can be blank.  */  
   State:string,
      /**  The zip or postal code portion of the shipping  address.  */  
   ZIP:string,
      /**  The country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  */  
   FaxNum:string,
      /**  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  */  
   PurPoint:string,
      /**  A  unique integer to identify vendors.  */  
   VendorNum:number,
      /**  The Service Call number that this Job is related to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is related to.  */  
   CallLine:number,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Packaging code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   FFCountryNum:number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress3:string,
      /**  Shipping, The country number of the Payer main address.  */  
   PayBTCountryNum:number,
      /**  Shipping, The phone number of the Payer main address.  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantity View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGCarrierCUIT  */  
   AGCarrierCUIT:string,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  AGTrackLicense  */  
   AGTrackLicense:string,
      /**  AGShippingWay  */  
   AGShippingWay:string,
      /**  Indicates if the Miscellaneous Shipment is a DMR Pack  */  
   IsDMRPack:boolean,
      /**  Dispatch Reason Code used for Customer Shipment  */  
   DispatchReason:string,
      /**  AGCOTMark  */  
   AGCOTMark:boolean,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  RMA Number linked to the Miscellaneous Shipment.  */  
   RMANum:number,
      /**  RMA Line linked to the Miscellaneous Shipment.  */  
   RMALine:number,
      /**  True if ready to send to FSA  */  
   FSAReady:boolean,
      /**  True if created as return shipment from RMA or DMR or Job  */  
   FromDepotRepair:boolean,
      /**  True if MscShpHd was created from Job Closing for Misc Shipment to WIP functionality.  */  
   FromJobClosing:boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  The sum of the vlaue of items in the carton.  */  
   CartonContentValue:number,
      /**  Carton Height  */  
   CartonHeight:number,
      /**  Carton length  */  
   CartonLength:number,
      /**  Carton Stage number  */  
   CartonStageNbr:string,
      /**  Carton width  */  
   CartonWidth:number,
   DspDigitalSignature:string,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  logical indicating if the weight prompt is enabled.  */  
   EnableWeight:boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Job Type Description  */  
   JobType:string,
      /**  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  */  
   LastCartonFlag:boolean,
   LegalNumberMessage:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   MasterpackPackNum:number,
      /**  Indicates if Customer is on credit Hold  */  
   OnCreditHold:boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   PkgLenEnable:number,
   PkgSizeUOMEnable:number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   PkgWidthEnable:number,
   ShipStatusDescription:string,
      /**  List delimited Address fields using the Address Format rules  */  
   AddrList:string,
   QSUseBOL:boolean,
   QSUseIntl:boolean,
   QSUseCO:boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   EnablePhantom:boolean,
      /**  Logical indicating if CartonTrkDtl records exist for this pack. Used by the UI for row rules.  */  
   PhantomCasesExist:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   CallLineLineDesc:string,
   CountryNumDescription:string,
   CustomerName:string,
   CustomerCustID:string,
   CustomerBTName:string,
   DeliveryTypeDescription:string,
   FreightedShipViaCodeWebDesc:string,
   FreightedShipViaCodeDescription:string,
   JobNumPartDescription:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PurPointPrimPCon:number,
   PurPointName:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointAddress3:string,
   PurPointAddress2:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointZip:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TranDocTypeDescription:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
   VendorNumCity:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   vrPONumShipToConName:string,
   vrPONumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MscShpUPSRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  UPS Quantity View Sequence  */  
   UPSQVSeq:number,
      /**  Email adress to be used for notifications.  */  
   EmailAddress:string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if the UPS quantum view is to be enabled.  */  
   EnableQuantumView:boolean,
   ShipStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipCOORow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  CountryNum for Country of Origin  */  
   OrigCountry:number,
      /**  Qty percent of this part which is from this country of origin.  */  
   QtyPerc:number,
      /**  Value percent of this part from this country of origin.  */  
   ValuePerc:number,
      /**  Is this the primary country of origin for this part  */  
   Primary:boolean,
      /**  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  */  
   RelatedToFile:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CountryDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtMiscShipTableset{
   MscShpHd:Erp_Tablesets_MscShpHdRow[],
   MscShpHdAttch:Erp_Tablesets_MscShpHdAttchRow[],
   MscShpDt:Erp_Tablesets_MscShpDtRow[],
   MscShpDtAttch:Erp_Tablesets_MscShpDtAttchRow[],
   ShipCOO:Erp_Tablesets_ShipCOORow[],
   MscShpUPS:Erp_Tablesets_MscShpUPSRow[],
   CartonTrkDtl:Erp_Tablesets_CartonTrkDtlRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateDigitalSignature_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GenerateDigitalSignature_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetAddrInfo_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetAddrInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param IUMCode
      @param Qty
   */  
export interface GetAllowsDecimals_input{
   IUMCode:string,
   Qty:string,
}

export interface GetAllowsDecimals_output{
   returnObj:boolean,
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param updatedField
      @param ds
   */  
export interface GetCallInfo_input{
      /**  Name of the field that changed, Order, Job, or PO  */  
   updatedField:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetCallInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPkgCode
   */  
export interface GetCartonPackaging_input{
   ipPkgCode:string,
}

export interface GetCartonPackaging_output{
parameters : {
      /**  output parameters  */  
   opPkgHeight:number,
   opPkgWidth:number,
   opPkgLength:number,
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ipDMRNum
      @param ds
   */  
export interface GetDMRSupplierInfo_input{
      /**  IPDMRNum DMR number supplied  */  
   ipDMRNum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetDMRSupplierInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDefaultUOM_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetDefaultUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_MscShpHdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMtlInfo_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetMtlInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param shipmentType
      @param packNum
   */  
export interface GetNewCartonTrkDtl_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   shipmentType:string,
   packNum:number,
}

export interface GetNewCartonTrkDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param packNum
      @param packLine
   */  
export interface GetNewMscShpDtAttch_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   packNum:number,
   packLine:number,
}

export interface GetNewMscShpDtAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewMscShpDt_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   packNum:number,
}

export interface GetNewMscShpDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewMscShpHdAttch_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   packNum:number,
}

export interface GetNewMscShpHdAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMscShpHd_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetNewMscShpHd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewMscShpUPS_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   packNum:number,
}

export interface GetNewMscShpUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param packNum
      @param packLine
   */  
export interface GetNewShipCOO_input{
   ds:Erp_Tablesets_MiscShipTableset[],
   relatedToFile:string,
   packNum:number,
   packLine:number,
}

export interface GetNewShipCOO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPONum
      @param ds
   */  
export interface GetPOSupplierInfo_input{
      /**  IPPONum PO number supplied  */  
   ipPONum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetPOSupplierInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPkgClass
      @param ds
   */  
export interface GetPackageClass_input{
      /**  package class to validate  */  
   ipPkgClass:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetPackageClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface GetPackaging_input{
      /**  package code  */  
   ipPkgCode:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetPackaging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipRMALine
      @param ds
   */  
export interface GetRMACustomerInfo_input{
      /**  ipRMALine RMA line supplied  */  
   ipRMALine:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetRMACustomerInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param whereClauseMscShpHd
      @param whereClauseMscShpHdAttch
      @param whereClauseMscShpDt
      @param whereClauseMscShpDtAttch
      @param whereClauseShipCOO
      @param whereClauseMscShpUPS
      @param whereClauseCartonTrkDtl
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMscShpHd:string,
   whereClauseMscShpHdAttch:string,
   whereClauseMscShpDt:string,
   whereClauseMscShpDtAttch:string,
   whereClauseShipCOO:string,
   whereClauseMscShpUPS:string,
   whereClauseCartonTrkDtl:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param workstationID
   */  
export interface GetScale_input{
   workstationID:string,
}

export interface GetScale_output{
parameters : {
      /**  output parameters  */  
   scaleID:string,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface GetTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface GetTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param pIUM
      @param ds
   */  
export interface OnChangeIUM_input{
      /**  IUM  */  
   pIUM:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangeIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param pdQty
      @param ds
   */  
export interface OnChangeQuantity_input{
      /**  Transaction Qty  */  
   pdQty:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangeQuantity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param iPackNum
      @param ipResetCODCharges
      @param ipResetInsCharges
   */  
export interface OpenCarton_input{
      /**  The carton number of the carton to open  */  
   iPackNum:number,
      /**  Indicates if the CODAmount is to be reset to zero  */  
   ipResetCODCharges:boolean,
      /**  Indicates if the DeclaredAmt is to be reset to zero  */  
   ipResetInsCharges:boolean,
}

export interface OpenCarton_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param packNum
   */  
export interface PrintSlip_input{
      /**  Packing Slip number  */  
   packNum:number,
}

export interface PrintSlip_output{
}

   /** Required : 
      @param ipQVEnable
      @param ds
   */  
export interface SetUPSQVEnable_input{
      /**  logical indicating if the quantum view is to enabled/disabled  */  
   ipQVEnable:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipShipStatus
      @param ds
   */  
export interface SetUPSQVShipStatus_input{
      /**  Shipment status  */  
   ipShipStatus:string,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface SetUPSQVShipStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param iPackNum
      @param ds
   */  
export interface StageCarton_input{
      /**  The carton number of the carton to Stage  */  
   iPackNum:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface StageCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMiscShipTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMiscShipTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ipAmountType
      @param ipAction
      @param ds
   */  
export interface UpdateManifestChargeAmts_input{
      /**  COD or DeclaredAmt  */  
   ipAmountType:string,
      /**  Yes = recalculate No = reset to zero  */  
   ipAction:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface UpdateManifestChargeAmts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPackNum
      @param ipCaseNum
      @param ipOldCOD
      @param ipCOD
      @param ipFlag
      @param ds
   */  
export interface UpdatePackCODWithCarton_input{
   ipPackNum:number,
   ipCaseNum:number,
   ipOldCOD:number,
   ipCOD:number,
   ipFlag:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface UpdatePackCODWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPackNum
      @param ipCaseNum
      @param ipOldDeclared
      @param ipDeclared
      @param ipDeclaredFlag
      @param ds
   */  
export interface UpdatePackDeclaredWithCarton_input{
   ipPackNum:number,
   ipCaseNum:number,
   ipOldDeclared:number,
   ipDeclared:number,
   ipDeclaredFlag:boolean,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface UpdatePackDeclaredWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ipPackNum
      @param ipOldWeight
      @param ipWeight
      @param ds
   */  
export interface UpdatePackWeightWithCarton_input{
   ipPackNum:number,
   ipOldWeight:number,
   ipWeight:number,
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface UpdatePackWeightWithCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MiscShipTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MiscShipTableset,
}
}

   /** Required : 
      @param iPackNum
   */  
export interface VoidCarton_input{
      /**  The carton number of the carton to void  */  
   iPackNum:number,
}

export interface VoidCarton_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}

   /** Required : 
      @param ipPackNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_MiscShipTableset[],
}


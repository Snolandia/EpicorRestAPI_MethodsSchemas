import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ARPIWriteOffSvc
// Description: A/P Promissory Note Write Off Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/$metadata", {
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
   Description: Get ARPIWriteOffs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPIWriteOffs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPIWriteOffs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPIWriteOffs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPIWriteOffs(requestBody:Erp_Tablesets_ARPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs", {
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
   Summary: Calls GetByID to retrieve the ARPIWriteOff item
   Description: Calls GetByID to retrieve the ARPIWriteOff item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNHeadRow
   */  
export function get_ARPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_ARPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPIWriteOff for the service
   Description: Calls UpdateExt to update ARPIWriteOff. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_ARPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete ARPIWriteOff item
   Description: Call UpdateExt to delete ARPIWriteOff item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
   Description: Get ARPNMoves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNMoves1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveRow
   */  
export function get_ARPIWriteOffs_Company_GroupID_HeadNum_ARPNMoves(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNMoves", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNMove item
   Description: Calls GetByID to retrieve the ARPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMove1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNMoveRow
   */  
export function get_ARPIWriteOffs_Company_GroupID_HeadNum_ARPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_ARPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ARPNMoves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNMoves
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveRow
   */  
export function get_ARPNMoves(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNMoves
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNMoveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNMoves(requestBody:Erp_Tablesets_ARPNMoveRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves", {
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
   Summary: Calls GetByID to retrieve the ARPNMove item
   Description: Calls GetByID to retrieve the ARPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNMoveRow
   */  
export function get_ARPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_ARPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNMove for the service
   Description: Calls UpdateExt to update ARPNMove. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, requestBody:Erp_Tablesets_ARPNMoveRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete ARPNMove item
   Description: Call UpdateExt to delete ARPNMove item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
   Description: Get ARPNMoveTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNMoveTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveTGLCRow
   */  
export function get_ARPNMoves_Company_GroupID_HeadNum_Seq_ARPNMoveTGLCs(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/ARPNMoveTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARPNMoveTGLC item
   Description: Calls GetByID to retrieve the ARPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMoveTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   */  
export function get_ARPNMoves_Company_GroupID_HeadNum_Seq_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, Seq:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")", {
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
         resolve(data as Erp_Tablesets_ARPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ARPNMoveTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNMoveTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveTGLCRow
   */  
export function get_ARPNMoveTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNMoveTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNMoveTGLCs(requestBody:Erp_Tablesets_ARPNMoveTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs", {
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
   Summary: Calls GetByID to retrieve the ARPNMoveTGLC item
   Description: Calls GetByID to retrieve the ARPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   */  
export function get_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, Seq:string, TGLCTranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")", {
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
         resolve(data as Erp_Tablesets_ARPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNMoveTGLC for the service
   Description: Calls UpdateExt to update ARPNMoveTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, Seq:string, TGLCTranNum:string, requestBody:Erp_Tablesets_ARPNMoveTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")", {
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
   Summary: Call UpdateExt to delete ARPNMoveTGLC item
   Description: Call UpdateExt to delete ARPNMoveTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param TGLCTranNum Desc: TGLCTranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company:string, GroupID:string, HeadNum:string, Seq:string, TGLCTranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")", {
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
   Description: Get ARPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNListRow
   */  
export function get_ARPNLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARPNLists(requestBody:Erp_Tablesets_ARPNListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists", {
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
   Summary: Calls GetByID to retrieve the ARPNList item
   Description: Calls GetByID to retrieve the ARPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARPNListRow
   */  
export function get_ARPNLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_ARPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARPNList for the service
   Description: Calls UpdateExt to update ARPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARPNLists_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_ARPNListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ARPNList item
   Description: Call UpdateExt to delete ARPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARPNLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseARPNHead:string, whereClauseARPNMove:string, whereClauseARPNMoveTGLC:string, whereClauseARPNList:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseARPNHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNHead=" + whereClauseARPNHead
   }
   if(typeof whereClauseARPNMove!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNMove=" + whereClauseARPNMove
   }
   if(typeof whereClauseARPNMoveTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNMoveTGLC=" + whereClauseARPNMoveTGLC
   }
   if(typeof whereClauseARPNList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARPNList=" + whereClauseARPNList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetList" + params, {
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
   Summary: Invoke method CheckGLInterface
   Description: Call this method once to validate the G/L Interface.  This method checks for
GLSyst availability and if G/L is interfaced with A/P. If A/P is not interfaced
with G/L then user should be asked if okay to continue without posting to G/L.
This method will return a Message for the user if not interfaced else the Message
is blank. If the user do not wish to continue then exit this object. This method
also returns a logical flag to indicate if Posting to G/L.  This value should be
passed on to each new A/P Adjustment (ARPNMove) record to process.
   OperationID: CheckGLInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGLInterface(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGLInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/CheckGLInterface", {
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
         resolve(data as CheckGLInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPNoteExisted
   OperationID: CheckPNoteExisted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPNoteExisted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNoteExisted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPNoteExisted(requestBody:CheckPNoteExisted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPNoteExisted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/CheckPNoteExisted", {
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
         resolve(data as CheckPNoteExisted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARPNList
   OperationID: GetARPNList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetARPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARPNList(requestBody:GetARPNList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetARPNList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetARPNList", {
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
         resolve(data as GetARPNList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
   OperationID: GetGroupIDForPI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPI(requestBody:GetGroupIDForPI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupIDForPI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetGroupIDForPI", {
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
         resolve(data as GetGroupIDForPI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNMove1
   Description: This method is to be used in place of GetNewARPNMove.  This method asks for
vendor number and invoice number to link the A/R Invoice Header (ARPNHead)
to A/R Invoice Adjustment (ARPNMove).
   OperationID: GetNewARPNMove1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNMove1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMove1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNMove1(requestBody:GetNewARPNMove1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNMove1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetNewARPNMove1", {
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
         resolve(data as GetNewARPNMove1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPNByID
   OperationID: GetPNByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPNByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPNByID(requestBody:GetPNByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPNByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetPNByID", {
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
         resolve(data as GetPNByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNHead(requestBody:GetNewARPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetNewARPNHead", {
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
         resolve(data as GetNewARPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNMove
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNMove(requestBody:GetNewARPNMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetNewARPNMove", {
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
         resolve(data as GetNewARPNMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARPNMoveTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNMoveTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARPNMoveTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMoveTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARPNMoveTGLC(requestBody:GetNewARPNMoveTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARPNMoveTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetNewARPNMoveTGLC", {
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
         resolve(data as GetNewARPNMoveTGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNMoveRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARPNMoveTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
   "BaseCurrSymbol":string,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "TermsDesc":string,
   "CurrencyDesc":string,
   "TotalCashReceived":number,
   "CompanyBankName":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CustomerBankName":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BillToName":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencySwitch":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocDiscount":number,
   "DocReceipt":number,
   "FullyPaid":boolean,
   "LegalNumMessage":string,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "XRateLabel":string,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3TranTaxAmt":number,
   "CompBankBranchCodeDesc":string,
   "CustBankBranchCodeDesc":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "GainLossReal":number,
   "GainLossUnreal":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "RevalueDate":string,
   "DocDiscountAmt":number,
   "Rpt1DiscountAmt":number,
   "Rpt2DiscountAmt":number,
   "Rpt3DiscountAmt":number,
   "Receipt":number,
   "Rpt1Receipt":number,
   "Rpt2Receipt":number,
   "Rpt3Receipt":number,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Type Description  */  
   "PITypeDescription":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
   "BankRecGainLoss":number,
   "DocBankRecGainLoss":number,
   "Rpt1BankRecGainLoss":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt3BankRecGainLoss":number,
   "BankTotalAmount":number,
   "StatusChgTranDocType":string,
   "StatusChgLegalNum":string,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Transaction Amount  */  
   "TranAmt":number,
      /**  Applied Amount  */  
   "AppliedAmt":number,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Base Amount  */  
   "BaseAmount":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  Company Bank Account ID  */  
   "CompBankAcctID":string,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Customer Bank Account ID  */  
   "CustBankAcctID":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Description  */  
   "Description":string,
      /**  Discount Amount. Base Currency.  */  
   "DiscountAmt":number,
      /**  Applied Amount. Document Currency.  */  
   "DocAppliedAmt":number,
      /**  Unapplied Amount. Document Currency.  */  
   "DocUnAppliedAmt":number,
      /**  Tax Amount. Document Currency.  */  
   "DocTaxAmt":number,
      /**  Transaction Amount. Document Currency.  */  
   "DocTranAmt":number,
      /**  Withholding Amount. Document Currency.  */  
   "DocWithholdAmt":number,
      /**  Exchange Rate  */  
   "ExchangeRate":number,
      /**  Get Default Tax ID's flag.  */  
   "GetDfltTaxIds":boolean,
      /**  Posted to GL flag  */  
   "GLPosted":boolean,
      /**  Legal Number  */  
   "LegalNumber":string,
      /**  Paid flag  */  
   "Paid":boolean,
      /**  Posted flag  */  
   "Posted":boolean,
      /**  Process Card  */  
   "ProcessCard":string,
      /**  Rate Group code  */  
   "RateGrpCode":string,
      /**  Recalculated before posting.  */  
   "RecalcBeforePost":boolean,
      /**  Applied Amount. Report Currency 1.  */  
   "Rpt1AppliedAmt":number,
      /**  Tax Amount. Report Currency 1.  */  
   "Rpt1TaxAmt":number,
      /**  Transaction Amount. Report Currency 1.  */  
   "Rpt1TranAmt":number,
      /**  Unapplied Amount. Report Currency 1.  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 1.  */  
   "Rpt1WithholdAmt":number,
      /**  Applied Amount. Report Currency 2.  */  
   "Rpt2AppliedAmt":number,
      /**  Tax Amount. Report Currency 2.  */  
   "Rpt2TaxAmt":number,
      /**  Transaction Amount. Report Currency 2.  */  
   "Rpt2TranAmt":number,
      /**  Unapplied Amount. Report Currency 2.  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 2.  */  
   "Rpt2WithholdAmt":number,
      /**  Applied Amount. Report Currency 3.  */  
   "Rpt3AppliedAmt":number,
      /**  Tax Amount. Report Currency 3.  */  
   "Rpt3TaxAmt":number,
      /**  Transaction Amount. Report Currency 3.  */  
   "Rpt3TranAmt":number,
      /**  Unapplied Amount. Report Currency 3.  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding Amount. Report Currency 3.  */  
   "Rpt3WithholdAmt":number,
      /**  Signed flag  */  
   "Signed":boolean,
      /**  Tax Amount. Base Currency.  */  
   "TaxAmt":number,
      /**  Tax Liability  */  
   "TaxRegionCode":string,
      /**  Total AR Amount  */  
   "TotalARAmt":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Unapplied Amount. Base Currency.  */  
   "UnappliedAmt":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  Withholding Amount. Base Currency.  */  
   "WithholdAmt":number,
      /**  Company Name  */  
   "CompanyName":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CustomerName":string,
      /**  First customer address line.  */  
   "CustomerAddr1":string,
      /**  Second customer address line.  */  
   "CustomerAddr2":string,
      /**  Third customer address line.  */  
   "CustomerAddr3":string,
      /**  Customer Stateportion of the address.  */  
   "CustomerState":string,
      /**  Customer City portion of the address.  */  
   "CustomerPostalCode":string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   "CustomerCity":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Reference to  invchead  */  
   "InvoiceNum":number,
      /**  AR Payment Instrument ID  */  
   "ARPromNoteID":string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   "FiscalPeriod":number,
      /**  The unique identifier of the fiscal calendar.  */  
   "FiscalCalendarID":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Transaction Type  */  
   "TranType":string,
      /**  Sent Flag  */  
   "Sent":boolean,
      /**  Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  IBANCode for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   "AutoGenerated":boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   "DirectDeposit":boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Customer's country code  */  
   "CustCountryCode":number,
      /**  Customer country portion of the address.  */  
   "CustomerCountry":string,
      /**  Promissory Note Status  */  
   "PIStatus":string,
      /**  Current Group  */  
   "CurGroupID":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Reason to change Company or Customer information  */  
   "ChgComment":string,
      /**  Hold from Application reason  */  
   "HoldReason":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Reference to reversed PI  */  
   "ReferseRef":number,
      /**  Reverse Date  */  
   "ReverseDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  TotalBankFee  */  
   "TotalBankFee":number,
      /**  DocTotalBankFee  */  
   "DocTotalBankFee":number,
      /**  Rpt1TotalBankFee  */  
   "Rpt1TotalBankFee":number,
      /**  Rpt2TotalBankFee  */  
   "Rpt2TotalBankFee":number,
      /**  Rpt3TotalBankFee  */  
   "Rpt3TotalBankFee":number,
      /**  OnAccount  */  
   "OnAccount":boolean,
      /**  Issuer Name  */  
   "IssuerName":string,
      /**  Signed By  */  
   "SignedBy":string,
      /**  Signed Date  */  
   "SignedDate":string,
      /**  Signee Address 1  */  
   "SigneeAddr1":string,
      /**  Signee Address 2  */  
   "SigneeAddr2":string,
      /**  Signee Address 3  */  
   "SigneeAddr3":string,
      /**  Signee City  */  
   "SigneeCity":string,
      /**  Signee State  */  
   "SigneeState":string,
      /**  Signee Postal Code  */  
   "SigneeZip":string,
      /**  Signee Country Number  */  
   "SigneeCountryNum":number,
      /**  Signee Phone  */  
   "SigneePhoneNum":string,
      /**  Signee Email Address  */  
   "SigneeEMailAddress":string,
      /**  Signee Comment  */  
   "SigneeComment":string,
      /**  DiscountChargeAmt  */  
   "DiscountChargeAmt":number,
      /**  DocDiscountChargeAmt  */  
   "DocDiscountChargeAmt":number,
      /**  Rpt1DiscountChargeAmt  */  
   "Rpt1DiscountChargeAmt":number,
      /**  Rpt2DiscountChargeAmt  */  
   "Rpt2DiscountChargeAmt":number,
      /**  Rpt3DiscountChargeAmt  */  
   "Rpt3DiscountChargeAmt":number,
      /**  Signee Bank Name  */  
   "SigneeBankName":string,
      /**  Signee Bank Account Number  */  
   "SigneeBankAcct":string,
      /**  Signee Bank Identifier  */  
   "SigneeBankIdentifier":string,
      /**  Signee IBAN Code  */  
   "SigneeIBANCode":string,
      /**  Signee Bank BranchCode  */  
   "SigneeBankBranchCode":string,
      /**  DiscountCashDate  */  
   "DiscountCashDate":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
   "ApplyDate":string,
   "BankCurrencyCode":string,
   "BankCurrSymbol":string,
   "BankRecGainLoss":number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   "calcRate":boolean,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
   "CompBankBranchCodeDesc":string,
      /**  Customer Credit Hold flag  */  
   "CreditHold":boolean,
   "CurrencyDesc":string,
   "CurrencySwitch":boolean,
   "CustBankBranchCodeDesc":string,
   "CustomerBankAcct":string,
   "CustomerBankIdentifier":string,
   "CustomerBankName":string,
   "DisableBankAcctIDPI":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
   "DocBankRecGainLoss":number,
   "DocDiscount":number,
   "DocDiscountAmt":number,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
   "DocReceipt":number,
      /**  Transaction Amount less Tax Amount  */  
   "DocTranTaxAmt":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
   "FullyPaid":boolean,
   "GainLossReal":number,
   "GainLossUnreal":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PIStatusDesc":string,
      /**  like PIType.Initiation  */  
   "PITypeInitiation":string,
   "Receipt":number,
   "RevalueDate":string,
   "Rpt1BankRecGainLoss":number,
   "Rpt1DiscountAmt":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt1Receipt":number,
   "Rpt1TranTaxAmt":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt2DiscountAmt":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt2Receipt":number,
   "Rpt2TranTaxAmt":number,
   "Rpt3BankRecGainLoss":number,
   "Rpt3DiscountAmt":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
   "Rpt3Receipt":number,
   "Rpt3TranTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "StatusChgLegalNum":string,
   "StatusChgTranDocType":string,
   "TermsDesc":string,
   "TotalCashReceived":number,
   "TotalRoundDiff":number,
   "TranTaxAmt":number,
   "TypeDesc":string,
   "XRateLabel":string,
   "BankTotalAmount":number,
   "BaseCurrencyCode":string,
   "BaseCurrencyDesc":string,
   "BaseCurrSymbol":string,
   "BillToName":string,
   "DocDiscountedAmt":number,
      /**  for kinetic purposes  */  
   "ARPNDtlExists":boolean,
      /**  for kinetic purposes  */  
   "ARPNDtlInvoicePosted":boolean,
   "BitFlag":number,
   "BankAcctDescription":string,
   "BankAcctBankName":string,
   "CashbookLineDescription":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CustNumInactive":boolean,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "PIStatusStatusDesc":string,
   "PITypeDescription":string,
   "RateGrpDescription":string,
   "TaxRegionCodeDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNListRow{
   "ARPromNoteID":string,
   "Company":string,
   "CurGroupID":string,
   "CustID":string,
   "GroupID":string,
   "HeadNum":number,
   "PIStage":string,
   "PIStatus":string,
   "TranAmt":number,
   "Type":string,
   "Selected":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNMoveRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Movement Order  */  
   "Seq":number,
      /**  Current Group ID  */  
   "CurGroupID":string,
      /**  Status  */  
   "PIStatus":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  Date created  */  
   "CreateDate":string,
      /**  Created By User  */  
   "CreateUser":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Move Type  */  
   "Type":string,
      /**  Comment  */  
   "Comment":string,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Creation Time  */  
   "CreateTime":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Reference to Endorsed AP PI GroupID.  */  
   "EndorsedAPPNGroupID":string,
      /**  Reference to Endorsed AP PI HeadNum.  */  
   "EndorsedAPPNHeadNum":number,
      /**  Description  */  
   "Description":string,
      /**  PI status description  */  
   "PIStatusDesc":string,
      /**  Posting Error Message  */  
   "PostErrMess":string,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
      /**  PI Type description  */  
   "TypeDesc":string,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARPNMoveTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  HeadNum for relation to ARPNMoveTGLC  */  
   "HeadNum":number,
      /**  Seq for relation to ARPNMoveTGLC  */  
   "Seq":number,
      /**  GroupID for relation to ARPNMoveTGLC  */  
   "GroupID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
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
export interface CheckGLInterface_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opPostToGL:boolean,
}
}

   /** Required : 
      @param ipID
   */  
export interface CheckPNoteExisted_input{
      /**  ipID  */  
   ipID:string,
}

export interface CheckPNoteExisted_output{
parameters : {
      /**  output parameters  */  
   opRet:string,
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARPIWriteOffTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNMove:Erp_Tablesets_ARPNMoveRow[],
   ARPNMoveTGLC:Erp_Tablesets_ARPNMoveTGLCRow[],
   ARPNList:Erp_Tablesets_ARPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
   BaseCurrSymbol:string,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   TermsDesc:string,
   CurrencyDesc:string,
   TotalCashReceived:number,
   CompanyBankName:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CustomerBankName:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BillToName:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencySwitch:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocDiscount:number,
   DocReceipt:number,
   FullyPaid:boolean,
   LegalNumMessage:string,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   XRateLabel:string,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
   Rpt1TranTaxAmt:number,
   Rpt2TranTaxAmt:number,
   Rpt3TranTaxAmt:number,
   CompBankBranchCodeDesc:string,
   CustBankBranchCodeDesc:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   GainLossReal:number,
   GainLossUnreal:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   RevalueDate:string,
   DocDiscountAmt:number,
   Rpt1DiscountAmt:number,
   Rpt2DiscountAmt:number,
   Rpt3DiscountAmt:number,
   Receipt:number,
   Rpt1Receipt:number,
   Rpt2Receipt:number,
   Rpt3Receipt:number,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Type Description  */  
   PITypeDescription:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
   BankRecGainLoss:number,
   DocBankRecGainLoss:number,
   Rpt1BankRecGainLoss:number,
   Rpt2BankRecGainLoss:number,
   Rpt3BankRecGainLoss:number,
   BankTotalAmount:number,
   StatusChgTranDocType:string,
   StatusChgLegalNum:string,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadListTableset{
   ARPNHeadList:Erp_Tablesets_ARPNHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  TotalBankFee  */  
   TotalBankFee:number,
      /**  DocTotalBankFee  */  
   DocTotalBankFee:number,
      /**  Rpt1TotalBankFee  */  
   Rpt1TotalBankFee:number,
      /**  Rpt2TotalBankFee  */  
   Rpt2TotalBankFee:number,
      /**  Rpt3TotalBankFee  */  
   Rpt3TotalBankFee:number,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  Issuer Name  */  
   IssuerName:string,
      /**  Signed By  */  
   SignedBy:string,
      /**  Signed Date  */  
   SignedDate:string,
      /**  Signee Address 1  */  
   SigneeAddr1:string,
      /**  Signee Address 2  */  
   SigneeAddr2:string,
      /**  Signee Address 3  */  
   SigneeAddr3:string,
      /**  Signee City  */  
   SigneeCity:string,
      /**  Signee State  */  
   SigneeState:string,
      /**  Signee Postal Code  */  
   SigneeZip:string,
      /**  Signee Country Number  */  
   SigneeCountryNum:number,
      /**  Signee Phone  */  
   SigneePhoneNum:string,
      /**  Signee Email Address  */  
   SigneeEMailAddress:string,
      /**  Signee Comment  */  
   SigneeComment:string,
      /**  DiscountChargeAmt  */  
   DiscountChargeAmt:number,
      /**  DocDiscountChargeAmt  */  
   DocDiscountChargeAmt:number,
      /**  Rpt1DiscountChargeAmt  */  
   Rpt1DiscountChargeAmt:number,
      /**  Rpt2DiscountChargeAmt  */  
   Rpt2DiscountChargeAmt:number,
      /**  Rpt3DiscountChargeAmt  */  
   Rpt3DiscountChargeAmt:number,
      /**  Signee Bank Name  */  
   SigneeBankName:string,
      /**  Signee Bank Account Number  */  
   SigneeBankAcct:string,
      /**  Signee Bank Identifier  */  
   SigneeBankIdentifier:string,
      /**  Signee IBAN Code  */  
   SigneeIBANCode:string,
      /**  Signee Bank BranchCode  */  
   SigneeBankBranchCode:string,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BankRecGainLoss:number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   CompBankBranchCodeDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencyDesc:string,
   CurrencySwitch:boolean,
   CustBankBranchCodeDesc:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
   CustomerBankName:string,
   DisableBankAcctIDPI:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocBankRecGainLoss:number,
   DocDiscount:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   Receipt:number,
   RevalueDate:string,
   Rpt1BankRecGainLoss:number,
   Rpt1DiscountAmt:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt1Receipt:number,
   Rpt1TranTaxAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2DiscountAmt:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt2Receipt:number,
   Rpt2TranTaxAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3DiscountAmt:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   Rpt3Receipt:number,
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TermsDesc:string,
   TotalCashReceived:number,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   TypeDesc:string,
   XRateLabel:string,
   BankTotalAmount:number,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   BaseCurrSymbol:string,
   BillToName:string,
   DocDiscountedAmt:number,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   CashbookLineDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CustNumInactive:boolean,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   PIStatusStatusDesc:string,
   PITypeDescription:string,
   RateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNListRow{
   ARPromNoteID:string,
   Company:string,
   CurGroupID:string,
   CustID:string,
   GroupID:string,
   HeadNum:number,
   PIStage:string,
   PIStatus:string,
   TranAmt:number,
   Type:string,
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNMoveRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Movement Order  */  
   Seq:number,
      /**  Current Group ID  */  
   CurGroupID:string,
      /**  Status  */  
   PIStatus:string,
      /**  Stage  */  
   PIStage:string,
      /**  Posted  */  
   Posted:boolean,
      /**  Date created  */  
   CreateDate:string,
      /**  Created By User  */  
   CreateUser:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Move Type  */  
   Type:string,
      /**  Comment  */  
   Comment:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Reference to Endorsed AP PI GroupID.  */  
   EndorsedAPPNGroupID:string,
      /**  Reference to Endorsed AP PI HeadNum.  */  
   EndorsedAPPNHeadNum:number,
      /**  Description  */  
   Description:string,
      /**  PI status description  */  
   PIStatusDesc:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
      /**  PI Type description  */  
   TypeDesc:string,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNMoveTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  HeadNum for relation to ARPNMoveTGLC  */  
   HeadNum:number,
      /**  Seq for relation to ARPNMoveTGLC  */  
   Seq:number,
      /**  GroupID for relation to ARPNMoveTGLC  */  
   GroupID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
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

export interface Erp_Tablesets_UpdExtARPIWriteOffTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ARPNMove:Erp_Tablesets_ARPNMoveRow[],
   ARPNMoveTGLC:Erp_Tablesets_ARPNMoveTGLCRow[],
   ARPNList:Erp_Tablesets_ARPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPNID
   */  
export interface GetARPNList_input{
      /**  ipPNID  */  
   ipPNID:string,
}

export interface GetARPNList_output{
   returnObj:Erp_Tablesets_ARPIWriteOffTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARPIWriteOffTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARPIWriteOffTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARPIWriteOffTableset[],
}

   /** Required : 
      @param arPromNoteID
   */  
export interface GetGroupIDForPI_input{
      /**  AR Promissory Note ID  */  
   arPromNoteID:string,
}

export interface GetGroupIDForPI_output{
parameters : {
      /**  output parameters  */  
   groupID:string,
   headNum:number,
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
   returnObj:Erp_Tablesets_ARPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewARPNHead_input{
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
   groupID:string,
}

export interface GetNewARPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param ipGroupID
      @param ipHeadNum
   */  
export interface GetNewARPNMove1_input{
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
      /**  The Group ID for this A/R Promissory Note Head  */  
   ipGroupID:string,
      /**  The A/R Promissory Note Head Number  */  
   ipHeadNum:number,
}

export interface GetNewARPNMove1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param seq
   */  
export interface GetNewARPNMoveTGLC_input{
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
   groupID:string,
   headNum:number,
   seq:number,
}

export interface GetNewARPNMoveTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewARPNMove_input{
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewARPNMove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}

   /** Required : 
      @param ipHeadNum
      @param ipPIType
      @param ipID
      @param ipCustID
      @param ipCurGroupID
      @param ipNewPIType
      @param ds
   */  
export interface GetPNByID_input{
      /**  ipHeadNum  */  
   ipHeadNum:number,
      /**  ipPIType  */  
   ipPIType:string,
      /**  ipID  */  
   ipID:string,
      /**  ipCustID  */  
   ipCustID:string,
      /**  ipCurGroupID  */  
   ipCurGroupID:string,
      /**  ipNewPIType  */  
   ipNewPIType:string,
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
}

export interface GetPNByID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}

   /** Required : 
      @param whereClauseARPNHead
      @param whereClauseARPNMove
      @param whereClauseARPNMoveTGLC
      @param whereClauseARPNList
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseARPNHead:string,
   whereClauseARPNMove:string,
   whereClauseARPNMoveTGLC:string,
   whereClauseARPNList:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARPIWriteOffTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARPIWriteOffTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARPIWriteOffTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARPIWriteOffTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARPIWriteOffTableset,
}
}


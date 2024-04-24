import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.SerialNoSvc
// Description: Update the SerialNo table. Update the Part Table for
Serial number format changes.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get SerialNoes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoes
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoRow
   */  
export function get_SerialNoes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNoes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes", {
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
   Summary: Calls GetByID to retrieve the SerialNo item
   Description: Calls GetByID to retrieve the SerialNo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   */  
export function get_SerialNoes_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNoRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialNoRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SerialNo for the service
   Description: Calls UpdateExt to update SerialNo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SerialNoes_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SerialNo item
   Description: Call UpdateExt to delete SerialNo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SerialNoes_Company_PartNum_SerialNumber(Company:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get SerialNoConditions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SerialNoConditions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoConditionRow
   */  
export function get_SerialNoes_Company_PartNum_SerialNumber_SerialNoConditions(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoConditions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SerialNoCondition item
   Description: Calls GetByID to retrieve the SerialNoCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoCondition1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param FSConditionID Desc: FSConditionID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   */  
export function get_SerialNoes_Company_PartNum_SerialNumber_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company:string, PartNum:string, SerialNumber:string, FSConditionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNoConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialNoConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SerialNoAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SerialNoAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoAttchRow
   */  
export function get_SerialNoes_Company_PartNum_SerialNumber_SerialNoAttches(Company:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SerialNoAttch item
   Description: Calls GetByID to retrieve the SerialNoAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   */  
export function get_SerialNoes_Company_PartNum_SerialNumber_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company:string, PartNum:string, SerialNumber:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNoAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoes(" + Company + "," + PartNum + "," + SerialNumber + ")/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialNoAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get SerialNoConditions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoConditions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoConditionRow
   */  
export function get_SerialNoConditions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoConditions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNoConditions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions", {
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
   Summary: Calls GetByID to retrieve the SerialNoCondition item
   Description: Calls GetByID to retrieve the SerialNoCondition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param FSConditionID Desc: FSConditionID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   */  
export function get_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company:string, PartNum:string, SerialNumber:string, FSConditionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNoConditionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialNoConditionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SerialNoCondition for the service
   Description: Calls UpdateExt to update SerialNoCondition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNoCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param FSConditionID Desc: FSConditionID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoConditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company:string, PartNum:string, SerialNumber:string, FSConditionID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SerialNoCondition item
   Description: Call UpdateExt to delete SerialNoCondition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNoCondition
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param FSConditionID Desc: FSConditionID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SerialNoConditions_Company_PartNum_SerialNumber_FSConditionID(Company:string, PartNum:string, SerialNumber:string, FSConditionID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoConditions(" + Company + "," + PartNum + "," + SerialNumber + "," + FSConditionID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get SerialNoAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNoAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoAttchRow
   */  
export function get_SerialNoAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNoAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNoAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches", {
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
   Summary: Calls GetByID to retrieve the SerialNoAttch item
   Description: Calls GetByID to retrieve the SerialNoAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNoAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   */  
export function get_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company:string, PartNum:string, SerialNumber:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialNoAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialNoAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SerialNoAttch for the service
   Description: Calls UpdateExt to update SerialNoAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNoAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialNoAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company:string, PartNum:string, SerialNumber:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete SerialNoAttch item
   Description: Call UpdateExt to delete SerialNoAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNoAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SerialNoAttches_Company_PartNum_SerialNumber_DrawingSeq(Company:string, PartNum:string, SerialNumber:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNoAttches(" + Company + "," + PartNum + "," + SerialNumber + "," + DrawingSeq + ")", {
          method: 'delete',
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialNoListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseSerialNo:string, whereClauseSerialNoAttch:string, whereClauseSerialNoCondition:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSerialNo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSerialNo=" + whereClauseSerialNo
   }
   if(typeof whereClauseSerialNoAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSerialNoAttch=" + whereClauseSerialNoAttch
   }
   if(typeof whereClauseSerialNoCondition!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSerialNoCondition=" + whereClauseSerialNoCondition
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, serialNumber:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof serialNumber!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serialNumber=" + serialNumber
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetList" + params, {
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

   /**  
   Summary: Invoke method ChangeAssemblySeq
   Description: Method to call when changing the AssemblySeq.
   OperationID: ChangeAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeAssemblySeq", {
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
   Summary: Invoke method ChangeAssemblySeqAssetCond
   Description: Method to call when changing the AssemblySeq in Mobile Asset Condition.
   OperationID: ChangeAssemblySeqAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssemblySeqAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssemblySeqAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAssemblySeqAssetCond(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeAssemblySeqAssetCond", {
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
   Summary: Invoke method ChangeCustomerID
   Description: Method to call when changing the CustID, passing a blank CustID clears the related fields.
   OperationID: ChangeCustomerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomerID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeCustomerID", {
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
   Summary: Invoke method ChangeDMRAction
   Description: Method to call when changing the DMRAction.
   OperationID: ChangeDMRAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDMRAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDMRAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDMRAction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeDMRAction", {
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
   Summary: Invoke method ChangeDMRNum
   Description: Method to call when changing the DMRNum, passing a 0 clears the related fields.
   OperationID: ChangeDMRNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDMRNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDMRNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDMRNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeDMRNum", {
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
   Summary: Invoke method ChangeJobNum
   Description: Method to call when changing the JobNum, passing a blank JobNum clears the related fields.
   OperationID: ChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeJobNum", {
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
   Summary: Invoke method ChangeJobNumAssetCond
   Description: Method to call when changing the JobNum in Mobile Asset Condition, passing a blank JobNum clears the related fields.
   OperationID: ChangeJobNumAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNumAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNumAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobNumAssetCond(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeJobNumAssetCond", {
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
   Summary: Invoke method ChangeMtlSeq
   Description: Method to call when changing the MtlSeq.
   OperationID: ChangeMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeMtlSeq", {
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
   Summary: Invoke method ChangeOprSeqAssetCond
   Description: Method to call when changing the OprSeq.
   OperationID: ChangeOprSeqAssetCond
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOprSeqAssetCond_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOprSeqAssetCond_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOprSeqAssetCond(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeOprSeqAssetCond", {
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
   Summary: Invoke method ChangePackLine
   Description: Method to call when changing the Ship To PackLine.
   OperationID: ChangePackLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePackLine", {
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
   Summary: Invoke method ChangePackNum
   Description: Method to call when changing the Ship To PackNum, passing 0 clears the PackLine.
   OperationID: ChangePackNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePackNum", {
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
   Summary: Invoke method ChangePackSlip
   Description: Method to call when changing the Receiving PackSlip, passing a blank PackSlip clears the PackSlipLine.
   OperationID: ChangePackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackSlip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePackSlip", {
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
   Summary: Invoke method ChangePackSlipLine
   Description: Method to call when changing the Receiving PackSlipLine.
   OperationID: ChangePackSlipLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackSlipLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackSlipLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePackSlipLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePackSlipLine", {
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
   Summary: Invoke method ChangePartNum
   Description: Call this method when the SerialNo.PartNum changes.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePartNum", {
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
   Summary: Invoke method ChangePCID
   Description: Call this method when the SerialNo.PCID changes.
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangePCID", {
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
   Summary: Invoke method ChangeRMALine
   Description: Method to call when changing the RMALine.
   OperationID: ChangeRMALine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMALine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeRMALine", {
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
   Summary: Invoke method ChangeRMANum
   Description: Method to call when changing the RMANum, passing a 0 clears the related fields.
   OperationID: ChangeRMANum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMANum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeRMANum", {
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
   Summary: Invoke method ChangeRMAReceipt
   Description: Method to call when changing the RMAReceipt.
   OperationID: ChangeRMAReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMAReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMAReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMAReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeRMAReceipt", {
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
   Summary: Invoke method ChangeShipToCustID
   Description: Method to call when changing the ShipToCustID.
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeShipToCustID", {
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
   Summary: Invoke method ChangeShipToNum
   Description: Method to call when changing the ShipToNum.
   OperationID: ChangeShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeShipToNum", {
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
   Summary: Invoke method ChangeUseOTS
   OperationID: ChangeUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeUseOTS", {
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
   Summary: Invoke method ChangeVendorID
   Description: Method to call when changing the VendorID, passing a blank VendorID clears the related fields.
   OperationID: ChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeVendorID", {
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
   Summary: Invoke method ChangeVendorPP
   Description: Method to call when changing the VendorPP.
   OperationID: ChangeVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorPP(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeVendorPP", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/FindPart", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetCodeDescList", {
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
   Summary: Invoke method GetPartFromRowId
   OperationID: GetPartFromRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetPartFromRowId", {
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
   Summary: Invoke method GetListForOperation
   Description: Purpose:  Call normal getlist and then filter out completed serial/operations
   OperationID: GetListForOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForOperation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetListForOperation", {
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
   Summary: Invoke method GetListInclReassigned
   Description: Purpose:  To find serial numbers related to a given job number.
   OperationID: GetListInclReassigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListInclReassigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListInclReassigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListInclReassigned(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetListInclReassigned", {
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
   Summary: Invoke method GetListCustom
   Description: Custom GetList method to allow sort by Customer ID and Name.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetListCustom", {
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
   Summary: Invoke method GetListServiceCall
   Description: Purpose:  Call normal getlist and then filter by given contract/line.
   OperationID: GetListServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetListServiceCall", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetRowsPerPlant
   Description: Gets the SerialNo dataset using a string with a WHERE clause and Plant as parameters to execute the query.
   OperationID: GetRowsPerPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPerPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetRowsPerPlant", {
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
   Summary: Invoke method GetRowsPerPlantKinetic
   Description: Gets the SerialNo dataset using Tracker parameters
   OperationID: GetRowsPerPlantKinetic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPlantKinetic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPlantKinetic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPerPlantKinetic(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetRowsPerPlantKinetic", {
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
   Summary: Invoke method GetRowsServiceCall
   Description: Purpose:  Gets the SerialNo dataset for Service Call Center
   OperationID: GetRowsServiceCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsServiceCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsServiceCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsServiceCall(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetRowsServiceCall", {
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
   Summary: Invoke method GetSerialsForCustShipTracker
   Description: Purpose:  To find serials that were shipped on a given pack number.
   OperationID: GetSerialsForCustShipTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialsForCustShipTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialsForCustShipTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialsForCustShipTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetSerialsForCustShipTracker", {
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
   Summary: Invoke method PlantSerialTracking
   Description: Verifies if the current login plant is set for Serial Tracking
   OperationID: PlantSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PlantSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantSerialTracking(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/PlantSerialTracking", {
          method: 'post',
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

   /**  
   Summary: Invoke method ChangeToData
   Description: Updates the ToCustNum and FullToShipToAddr fields, based either on the OTS status and OrderNum or the CustID/ShipTo
   OperationID: ChangeToData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ChangeToData", {
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
   Summary: Invoke method FormatOTSAddress
   Description: Updates FullToShipToAddr with the data stored on the OTS Fields (display only)
   OperationID: FormatOTSAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FormatOTSAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FormatOTSAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FormatOTSAddress(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/FormatOTSAddress", {
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
   Summary: Invoke method SerialNumberExists
   Description: Verifies if a Serial Number exists in the Database.
   OperationID: SerialNumberExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SerialNumberExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SerialNumberExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNumberExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/SerialNumberExists", {
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
   Summary: Invoke method GetRowsPerPCID
   Description: Gets the SerialNo dataset by PCID. This method will search for any PCID child items and retrieve their SerialNo.
   OperationID: GetRowsPerPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPerPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPerPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPerPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetRowsPerPCID", {
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
   Summary: Invoke method GetSerialsForJobTracker
   Description: Purpose:  To find serials that were ever associated with a given job number.
   OperationID: GetSerialsForJobTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialsForJobTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialsForJobTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialsForJobTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetSerialsForJobTracker", {
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
   Summary: Invoke method GetSerialNumbersNotCompleted
   Description: Gets serial numbers not completed
   OperationID: GetSerialNumbersNotCompleted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumbersNotCompleted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumbersNotCompleted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumbersNotCompleted(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetSerialNumbersNotCompleted", {
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
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/ValidateOTSTaxID", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/OnChangingAttributeSet", {
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
   Summary: Invoke method GetNewSerialNo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialNo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetNewSerialNo", {
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
   Summary: Invoke method GetNewSerialNoAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNoAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNoAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNoAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialNoAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetNewSerialNoAttch", {
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
   Summary: Invoke method GetNewSerialNoCondition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialNoCondition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNoCondition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNoCondition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialNoCondition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetNewSerialNoCondition", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialNoAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoConditionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialNoConditionRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialNoListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialNoRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialNoRow[],
}

export interface Erp_Tablesets_SerialNoAttchRow{
   "Company":string,
   "PartNum":string,
   "SerialNumber":string,
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

export interface Erp_Tablesets_SerialNoConditionRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   "SerialNumber":string,
      /**  System Generated Unique ID  */  
   "FSConditionID":number,
      /**  Date condition was observed  */  
   "FSConditionDate":string,
      /**  Condition Code entry field  */  
   "FSAssetConditionCode":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this serial no condition applies.  */  
   "OprSeq":number,
      /**  Field for recording additional details about the asset condition which explain why it has taken the value assigned.  For example, if the asset condition is fully serviceable but requires attention at next service the text box might have an entry like 'Hydraulic ram rubber boot split: will require replacement during next service'  */  
   "FSAdditionalDetails":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SerialNoListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   "SerialNumber":string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   "SNStatus":string,
      /**  Job number.  The job number that this item is linked to.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Seq # of specific material or subcontract operation record.  */  
   "MtlSeq":number,
      /**  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  */  
   "PackNum":number,
      /**  The packing slip line that this serial numbered item shipped on.  */  
   "PackLine":number,
      /**  Indicates that this serial number has been voided.  */  
   "Voided":boolean,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   "Scrapped":boolean,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackSlipLine":number,
      /**  The status of this serial numbered item prior to its current status.  */  
   "PrevSNStatus":string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   "SNBaseNumber":string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   "ScrapReasonCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   "SNReference":string,
      /**  Return Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line # of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA receipt  */  
   "RMAReceipt":number,
      /**  DMR Number to identify the DMR record.  */  
   "DMRNum":number,
      /**  DMR action number.  */  
   "DMRActionNum":number,
      /**  Indicates that this item has failed inspection.  */  
   "FailSelect":boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   "LineDetailNum":number,
      /**  Used to tie back to the related RMADisp record.  */  
   "RMADisp":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfNum":number,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "WarrExpiration":string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   "ShippedFrom":string,
      /**  Added at shipment  */  
   "TranAdd":boolean,
      /**  Transfer Order packing slip.  */  
   "TFPackNum":number,
      /**  Transfer Order packing slip Line.  */  
   "TFPackLine":number,
      /**  Related (OrderHed) Sales Order number  */  
   "OrderNum":number,
      /**  Related (OrderDtl) sales order line number  */  
   "OrderLine":number,
      /**  related (OrderRel) order release number  */  
   "OrderRelNum":number,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   "FullyMatched":boolean,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   "AddedByMatching":boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   "SubConOprSeq":number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborHedSeq":number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborDtlSeq":number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   "LastLbrOprSeq":number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   "LotNum":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Cross Reference Part Type  */  
   "XRefPartType":string,
      /**  Cross Reference Part Number  */  
   "XRefPartNum":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Next Labor Operation Sequence  */  
   "NextLbrAssySeq":number,
      /**  Next Labor Assembly Sequence  */  
   "NextLbrOprSeq":number,
      /**  Latitude of Mobile FS Asset  */  
   "Latitude":number,
      /**  Longitude of Mobile FS Asset  */  
   "Longitude":number,
      /**  Altitude of Mobile FS Asset  */  
   "Altitude":number,
      /**  Class Code Entry Field  */  
   "FSAssetClassCode":string,
      /**  Field Service Level Agreement Text  */  
   "FSServiceLevelAgreement":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Related (TFOrdHed) Transfer Order number  */  
   "TFOrdNum":string,
      /**  Related (TFOrdLine) Transfer Order Line number  */  
   "TFOrdLine":number,
      /**  Logical indicating the current serial number is selected for the current transaction.  Flag indicating the UI/BL needs to process this serial number.  */  
   "SelectedForCurrentTran":boolean,
      /**  Scrap Reason Code Description  */  
   "ScrapReasonCodeDesc":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Vendor ID  */  
   "VendorID":string,
      /**  CustIDBTName  */  
   "CustIDBTName":string,
      /**  CustIDCustID  */  
   "CustIDCustID":string,
      /**  CustIDName  */  
   "CustIDName":string,
      /**  VendorIDAddress1  */  
   "VendorIDAddress1":string,
      /**  VendorIDAddress2  */  
   "VendorIDAddress2":string,
      /**  VendorIDAddress3  */  
   "VendorIDAddress3":string,
      /**  VendorIDCity  */  
   "VendorIDCity":string,
      /**  VendorIDCountry  */  
   "VendorIDCountry":string,
      /**  VendorIDCurrencyCode  */  
   "VendorIDCurrencyCode":string,
      /**  VendorIDDefaultFOB  */  
   "VendorIDDefaultFOB":string,
      /**  VendorIDName  */  
   "VendorIDName":string,
      /**  VendorIDState  */  
   "VendorIDState":string,
      /**  VendorIDTermsCode  */  
   "VendorIDTermsCode":string,
      /**  VendorIDVendorID  */  
   "VendorIDVendorID":string,
      /**  VendorIDZIP  */  
   "VendorIDZIP":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SerialNoRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   "SerialNumber":string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   "SNStatus":string,
      /**  Job number.  The job number that this item is linked to.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Seq # of specific material or subcontract operation record.  */  
   "MtlSeq":number,
      /**  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  */  
   "PackNum":number,
      /**  The packing slip line that this serial numbered item shipped on.  */  
   "PackLine":number,
      /**  Indicates that this serial number has been voided.  */  
   "Voided":boolean,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   "Scrapped":boolean,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackSlipLine":number,
      /**  if false idicates that this record can be used.  */  
   "Selected":boolean,
      /**  The status of this serial numbered item prior to its current status.  */  
   "PrevSNStatus":string,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   "SNPrefix":string,
      /**  Format of the Base number.  */  
   "SNFormat":string,
      /**  Information about serail number formatting.  */  
   "SNBaseStructure":string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   "SNBaseNumber":string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   "ScrapReasonCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   "SNReference":string,
      /**  Return Authorization Number of related RMAHead.  */  
   "RMANum":number,
      /**  Line # of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMA receipt  */  
   "RMAReceipt":number,
      /**  DMR Number to identify the DMR record.  */  
   "DMRNum":number,
      /**  The date that this serial numbered was created.  */  
   "CreateDate":string,
      /**  DMR action number.  */  
   "DMRActionNum":number,
      /**  Indicates that this item has failed inspection.  */  
   "FailSelect":boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   "LineDetailNum":number,
      /**  Used to tie back to the related RMADisp record.  */  
   "RMADisp":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfNum":number,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "WarrExpiration":string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Modified By  */  
   "ModifiedBy":string,
      /**  Modification Date  */  
   "ModifiedDate":string,
      /**  Modification Time  */  
   "ModifiedTime":number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   "ShippedFrom":string,
      /**  Added at shipment  */  
   "TranAdd":boolean,
      /**  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  */  
   "TempTranID":number,
      /**  Transfer Order packing slip.  */  
   "TFPackNum":number,
      /**  Transfer Order packing slip Line.  */  
   "TFPackLine":number,
      /**  Related (OrderHed) Sales Order number  */  
   "OrderNum":number,
      /**  Related (OrderDtl) sales order line number  */  
   "OrderLine":number,
      /**  related (OrderRel) order release number  */  
   "OrderRelNum":number,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   "FullyMatched":boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   "SNMask":string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   "AddedByMatching":boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   "SubConOprSeq":number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborHedSeq":number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborDtlSeq":number,
      /**  Indicates which Site?s SNFormat data was used to generate this serial number.  */  
   "CreatedInPlant":string,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   "LastLbrOprSeq":number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   "LotNum":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Cross Reference Part Type  */  
   "XRefPartType":string,
      /**  Cross Reference Part Number  */  
   "XRefPartNum":string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Next Labor Operation Sequence  */  
   "NextLbrAssySeq":number,
      /**  Next Labor Assembly Sequence  */  
   "NextLbrOprSeq":number,
      /**  Latitude of Mobile FS Asset  */  
   "Latitude":number,
      /**  Longitude of Mobile FS Asset  */  
   "Longitude":number,
      /**  Altitude of Mobile FS Asset  */  
   "Altitude":number,
      /**  Class Code Entry Field  */  
   "FSAssetClassCode":string,
      /**  Field Service Level Agreement Text  */  
   "FSServiceLevelAgreement":string,
      /**  Accuracy  */  
   "Accuracy":number,
      /**  MeterReading  */  
   "MeterReading":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  One time shipto flag  */  
   "OTS":boolean,
      /**  OTS Address 1  */  
   "OTSAddress1":string,
      /**  OTS Address 2  */  
   "OTSAddress2":string,
      /**  OTS Address 3  */  
   "OTSAddress3":string,
      /**  OTS City  */  
   "OTSCity":string,
      /**  OTS Contact  */  
   "OTSContact":string,
      /**  OTS Country Number  */  
   "OTSCountryNum":number,
      /**  OTS Country Number  */  
   "OTSCustSaved":boolean,
      /**  One Time fax number  */  
   "OTSFaxNum":string,
      /**  OTS Name  */  
   "OTSName":string,
      /**  OTS Phone Number  */  
   "OTSPhoneNum":string,
      /**  OTS Resale ID  */  
   "OTSResaleID":string,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  OTS Ship To Num  */  
   "OTSShipToNum":string,
      /**  OTS State  */  
   "OTSState":string,
      /**  OTS Tax Region Code  */  
   "OTSTaxRegionCode":string,
      /**  OTS Zip  */  
   "OTSZip":string,
      /**  PriorJobNum  */  
   "PriorJobNum":string,
      /**  PriorAssemblySeq  */  
   "PriorAssemblySeq":number,
      /**  PriorMtlSeq  */  
   "PriorMtlSeq":number,
      /**  PriorPartNum  */  
   "PriorPartNum":string,
      /**  PCID  */  
   "PCID":string,
      /**  Misc Shipment Pack Num if related to a misc shipment  */  
   "MscPackNum":number,
      /**  Misc Shipment Pack Line if related to a Misc Shipment  */  
   "MscPackLine":number,
      /**  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   "AssetNum":string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   "AdditionNum":number,
      /**  DisposalNum  */  
   "DisposalNum":number,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Related (TFOrdHed) Transfer Order number  */  
   "TFOrdNum":string,
      /**  Related (TFOrdLine) Transfer Order Line number  */  
   "TFOrdLine":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "AllowOTS":boolean,
      /**  Customer ID  */  
   "CustID":string,
      /**  CustIDBTName  */  
   "CustIDBTName":string,
      /**  CustIDCustID  */  
   "CustIDCustID":string,
      /**  CustIDName  */  
   "CustIDName":string,
   "OTSSaved":boolean,
      /**  Scrap reason code description  */  
   "ScrapReasonCodeDesc":string,
      /**  Shipt To Customer ID  */  
   "ShipToCustID":string,
   "ShipToName":string,
      /**  INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED  */  
   "SNStatusTrans":string,
      /**  Source of transaction  */  
   "TransactionSource":string,
      /**  Vendor ID  */  
   "VendorID":string,
      /**  VendorIDAddress1  */  
   "VendorIDAddress1":string,
      /**  VendorIDAddress2  */  
   "VendorIDAddress2":string,
      /**  VendorIDAddress3  */  
   "VendorIDAddress3":string,
      /**  VendorIDCity  */  
   "VendorIDCity":string,
      /**  VendorIDCountry  */  
   "VendorIDCountry":string,
      /**  VendorIDCurrencyCode  */  
   "VendorIDCurrencyCode":string,
      /**  VendorIDDefaultFOB  */  
   "VendorIDDefaultFOB":string,
      /**  VendorIDName  */  
   "VendorIDName":string,
      /**  VendorIDState  */  
   "VendorIDState":string,
      /**  VendorIDTermsCode  */  
   "VendorIDTermsCode":string,
      /**  VendorIDVendorID  */  
   "VendorIDVendorID":string,
      /**  VendorIDZIP  */  
   "VendorIDZIP":string,
      /**  Displays formatted full from ship address. Only for information cannot be modified  */  
   "FullFromShipToAddr":string,
      /**  Displays formatted full to ship address. Only for information cannot be modified  */  
   "FullToShipToAddr":string,
      /**  External field to define the Customer to which we want to transfer the serial number  */  
   "ToCustID":string,
      /**  External field to define the Customer to which we want to transfer the serial number  */  
   "ToCustNum":number,
      /**  External field to define the Ship to ID,  to which we want to transfer the serial number  */  
   "ToShipToNum":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CustNumInactive":boolean,
   "CustNumBTName":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumName":string,
   "CustNumCustID":string,
   "DMRNumPartDescription":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "FSAssetClassCodeFSAssetClassDesc":string,
   "MtlSeqDescription":string,
   "MtlSeqSalvageDescription":string,
   "NonConfNumDescription":string,
   "OTSCntryISOCode":string,
   "OTSCntryDescription":string,
   "OTSCntryEUMember":boolean,
   "PackNumShipStatus":string,
   "PartNumAttrClassID":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PurPointAddress1":string,
   "PurPointAddress3":string,
   "PurPointAddress2":string,
   "PurPointCountry":string,
   "PurPointZip":string,
   "PurPointCity":string,
   "PurPointState":string,
   "PurPointName":string,
   "PurPointPrimPCon":number,
   "RMALineLineDesc":string,
   "ScrapReasonCodeDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskDescription":string,
   "ShipToCustName":string,
   "ShipToCustNumInactive":boolean,
   "ShipToNumInactive":boolean,
   "TaxRegionCodeDescription":string,
   "VendorNumAddress2":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumName":string,
   "VendorNumAddress1":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress3":string,
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedAsmSeq
      @param ds
   */  
export interface ChangeAssemblySeqAssetCond_input{
      /**  The proposed Job Assembly Seq  */  
   proposedAsmSeq:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeAssemblySeqAssetCond_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedAsmSeq
      @param ds
   */  
export interface ChangeAssemblySeq_input{
      /**  The proposed Job Assembly Seq  */  
   proposedAsmSeq:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedCustID
      @param ds
   */  
export interface ChangeCustomerID_input{
      /**  The proposed Customer ID  */  
   proposedCustID:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeCustomerID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedDMRAction
      @param ds
   */  
export interface ChangeDMRAction_input{
      /**  The proposed DMR Action  */  
   proposedDMRAction:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeDMRAction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedDMRNum
      @param ds
   */  
export interface ChangeDMRNum_input{
      /**  The proposed DMR Number  */  
   proposedDMRNum:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeDMRNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedJobNum
      @param ds
   */  
export interface ChangeJobNumAssetCond_input{
      /**  The proposed Job Number  */  
   proposedJobNum:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeJobNumAssetCond_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedJobNum
      @param ds
   */  
export interface ChangeJobNum_input{
      /**  The proposed Job Number  */  
   proposedJobNum:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedMtlSeq
      @param ds
   */  
export interface ChangeMtlSeq_input{
      /**  The proposed Job Assembly Seq  */  
   proposedMtlSeq:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedOprSeq
      @param ds
   */  
export interface ChangeOprSeqAssetCond_input{
      /**  The proposed Job Opr Seq  */  
   proposedOprSeq:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeOprSeqAssetCond_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param pcProposedPCID
      @param ds
   */  
export interface ChangePCID_input{
      /**  The proposed PCID  */  
   pcProposedPCID:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedPackLine
      @param ds
   */  
export interface ChangePackLine_input{
      /**  The proposed Ship To Pack Line  */  
   proposedPackLine:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePackLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedPackNum
      @param ds
   */  
export interface ChangePackNum_input{
      /**  The proposed Ship To Packing Number  */  
   proposedPackNum:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePackNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedPackSlipLine
      @param ds
   */  
export interface ChangePackSlipLine_input{
      /**  The proposed Receiving Packing Slip Line  */  
   proposedPackSlipLine:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePackSlipLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedPackSlip
      @param ds
   */  
export interface ChangePackSlip_input{
      /**  The proposed Receiving Packing Slip  */  
   proposedPackSlip:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePackSlip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param pcProposedPartNum
      @param ds
   */  
export interface ChangePartNum_input{
      /**  The proposed Part Number  */  
   pcProposedPartNum:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedRMALine
      @param ds
   */  
export interface ChangeRMALine_input{
      /**  The proposed RMA Line  */  
   proposedRMALine:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeRMALine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedRMANum
      @param ds
   */  
export interface ChangeRMANum_input{
      /**  The proposed RMA Number  */  
   proposedRMANum:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeRMANum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedRMAReceipt
      @param ds
   */  
export interface ChangeRMAReceipt_input{
      /**  The proposed RMA Receipt  */  
   proposedRMAReceipt:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeRMAReceipt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedShipToCustID
      @param ds
   */  
export interface ChangeShipToCustID_input{
      /**  /// The proposed Ship To CustID  */  
   proposedShipToCustID:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeShipToNum_input{
      /**  The proposed Ship To Number  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param CustID
      @param ShipTo
      @param OrderNum
      @param OrderLine
      @param OrderRelNum
      @param ds
   */  
export interface ChangeToData_input{
   CustID:string,
   ShipTo:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeToData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUseOTS_input{
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedVendorID
      @param ds
   */  
export interface ChangeVendorID_input{
      /**  The proposed Vendor ID  */  
   proposedVendorID:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param proposedPurPoint
      @param ds
   */  
export interface ChangeVendorPP_input{
      /**  The proposed Vendor Purchase Point  */  
   proposedPurPoint:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface ChangeVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param partNum
      @param serialNumber
   */  
export interface DeleteByID_input{
   partNum:string,
   serialNumber:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AltSerialNORow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   SerialNumber:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Job number.  The job number that this item is linked to.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   MtlSeq:number,
      /**  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  */  
   PackNum:number,
      /**  The packing slip line that this serial numbered item shipped on.  */  
   PackLine:number,
      /**  Indicates that this serial number has been voided.  */  
   Voided:boolean,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   Scrapped:boolean,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackSlipLine:number,
      /**  if false idicates that this record can be used.  */  
   Selected:boolean,
      /**  The status of this serial numbered item prior to its current status.  */  
   PrevSNStatus:string,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   SNPrefix:string,
      /**  Format of the Base number.  */  
   SNFormat:string,
      /**  Information about serail number formatting.  */  
   SNBaseStructure:string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   SNBaseNumber:string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   ScrapReasonCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   SNReference:string,
      /**  Return Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line # of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA receipt  */  
   RMAReceipt:number,
      /**  DMR Number to identify the DMR record.  */  
   DMRNum:number,
      /**  The date that this serial numbered was created.  */  
   CreateDate:string,
      /**  DMR action number.  */  
   DMRActionNum:number,
      /**  Indicates that this item has failed inspection.  */  
   FailSelect:boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   LineDetailNum:number,
      /**  Used to tie back to the related RMADisp record.  */  
   RMADisp:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfNum:number,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The latest of the 3 warranty expiration dates  */  
   WarrExpiration:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  Modified By  */  
   ModifiedBy:string,
      /**  Modification Date  */  
   ModifiedDate:string,
      /**  Modification Time  */  
   ModifiedTime:number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   ShippedFrom:string,
      /**  Added at shipment  */  
   TranAdd:boolean,
      /**  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  */  
   TempTranID:number,
      /**  Transfer Order packing slip.  */  
   TFPackNum:number,
      /**  Transfer Order packing slip Line.  */  
   TFPackLine:number,
      /**  Related (OrderHed) Sales Order number  */  
   OrderNum:number,
      /**  Related (OrderDtl) sales order line number  */  
   OrderLine:number,
      /**  related (OrderRel) order release number  */  
   OrderRelNum:number,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   FullyMatched:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   SNMask:string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   AddedByMatching:boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   SubConOprSeq:number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborHedSeq:number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborDtlSeq:number,
      /**  Indicates which Site?s SNFormat data was used to generate this serial number.  */  
   CreatedInPlant:string,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   LastLbrOprSeq:number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Cross Reference Part Type  */  
   XRefPartType:string,
      /**  Cross Reference Part Number  */  
   XRefPartNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Next Labor Operation Sequence  */  
   NextLbrAssySeq:number,
      /**  Next Labor Assembly Sequence  */  
   NextLbrOprSeq:number,
      /**  Latitude of Mobile FS Asset  */  
   Latitude:number,
      /**  Longitude of Mobile FS Asset  */  
   Longitude:number,
      /**  Altitude of Mobile FS Asset  */  
   Altitude:number,
      /**  Class Code Entry Field  */  
   FSAssetClassCode:string,
      /**  Field Service Level Agreement Text  */  
   FSServiceLevelAgreement:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AssetNum:string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AdditionNum:number,
      /**  DisposalNum  */  
   DisposalNum:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Related (TFOrdHed) Transfer Order number  */  
   TFOrdNum:string,
      /**  Related (TFOrdLine) Transfer Order Line number  */  
   TFOrdLine:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   CustID:string,
   CustIDName:string,
   Description:string,
   ScrapReasonCodeDesc:string,
   ShipToCustID:string,
   TransactionSource:string,
   VendorID:string,
   VendorIDCurrencyCode:string,
   VendorIDName:string,
   VendorIDTermsCode:string,
   VendorIDVendorID:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CustNumCustID:string,
   CustNumBTName:string,
   CustNumName:string,
   DMRNumPartDescription:string,
   MtlSeqDescription:string,
   MtlSeqSalvageDescription:string,
   NonConfNumDescription:string,
   PackNumShipStatus:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PurPointAddress3:string,
   PurPointCountry:string,
   PurPointState:string,
   PurPointName:string,
   PurPointZip:string,
   PurPointPrimPCon:number,
   PurPointAddress2:string,
   PurPointAddress1:string,
   PurPointCity:string,
   RMALineLineDesc:string,
   ScrapReasonCodeDescription:string,
   SerialMaskDescription:string,
   SerialMaskMaskType:number,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumAddress1:string,
   VendorNumDefaultFOB:string,
   VendorNumVendorID:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AltSerialNoTableset{
   AltSerialNO:Erp_Tablesets_AltSerialNORow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SerialNoAttchRow{
   Company:string,
   PartNum:string,
   SerialNumber:string,
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

export interface Erp_Tablesets_SerialNoConditionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   SerialNumber:string,
      /**  System Generated Unique ID  */  
   FSConditionID:number,
      /**  Date condition was observed  */  
   FSConditionDate:string,
      /**  Condition Code entry field  */  
   FSAssetConditionCode:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  The sequence of the operation record within the specific Job/Assembly to which this serial no condition applies.  */  
   OprSeq:number,
      /**  Field for recording additional details about the asset condition which explain why it has taken the value assigned.  For example, if the asset condition is fully serviceable but requires attention at next service the text box might have an entry like 'Hydraulic ram rubber boot split: will require replacement during next service'  */  
   FSAdditionalDetails:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNoListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   SerialNumber:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Job number.  The job number that this item is linked to.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   MtlSeq:number,
      /**  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  */  
   PackNum:number,
      /**  The packing slip line that this serial numbered item shipped on.  */  
   PackLine:number,
      /**  Indicates that this serial number has been voided.  */  
   Voided:boolean,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   Scrapped:boolean,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackSlipLine:number,
      /**  The status of this serial numbered item prior to its current status.  */  
   PrevSNStatus:string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   SNBaseNumber:string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   ScrapReasonCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   SNReference:string,
      /**  Return Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line # of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA receipt  */  
   RMAReceipt:number,
      /**  DMR Number to identify the DMR record.  */  
   DMRNum:number,
      /**  DMR action number.  */  
   DMRActionNum:number,
      /**  Indicates that this item has failed inspection.  */  
   FailSelect:boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   LineDetailNum:number,
      /**  Used to tie back to the related RMADisp record.  */  
   RMADisp:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfNum:number,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The latest of the 3 warranty expiration dates  */  
   WarrExpiration:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   ShippedFrom:string,
      /**  Added at shipment  */  
   TranAdd:boolean,
      /**  Transfer Order packing slip.  */  
   TFPackNum:number,
      /**  Transfer Order packing slip Line.  */  
   TFPackLine:number,
      /**  Related (OrderHed) Sales Order number  */  
   OrderNum:number,
      /**  Related (OrderDtl) sales order line number  */  
   OrderLine:number,
      /**  related (OrderRel) order release number  */  
   OrderRelNum:number,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   FullyMatched:boolean,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   AddedByMatching:boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   SubConOprSeq:number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborHedSeq:number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborDtlSeq:number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   LastLbrOprSeq:number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Cross Reference Part Type  */  
   XRefPartType:string,
      /**  Cross Reference Part Number  */  
   XRefPartNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Next Labor Operation Sequence  */  
   NextLbrAssySeq:number,
      /**  Next Labor Assembly Sequence  */  
   NextLbrOprSeq:number,
      /**  Latitude of Mobile FS Asset  */  
   Latitude:number,
      /**  Longitude of Mobile FS Asset  */  
   Longitude:number,
      /**  Altitude of Mobile FS Asset  */  
   Altitude:number,
      /**  Class Code Entry Field  */  
   FSAssetClassCode:string,
      /**  Field Service Level Agreement Text  */  
   FSServiceLevelAgreement:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Related (TFOrdHed) Transfer Order number  */  
   TFOrdNum:string,
      /**  Related (TFOrdLine) Transfer Order Line number  */  
   TFOrdLine:number,
      /**  Logical indicating the current serial number is selected for the current transaction.  Flag indicating the UI/BL needs to process this serial number.  */  
   SelectedForCurrentTran:boolean,
      /**  Scrap Reason Code Description  */  
   ScrapReasonCodeDesc:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Vendor ID  */  
   VendorID:string,
      /**  CustIDBTName  */  
   CustIDBTName:string,
      /**  CustIDCustID  */  
   CustIDCustID:string,
      /**  CustIDName  */  
   CustIDName:string,
      /**  VendorIDAddress1  */  
   VendorIDAddress1:string,
      /**  VendorIDAddress2  */  
   VendorIDAddress2:string,
      /**  VendorIDAddress3  */  
   VendorIDAddress3:string,
      /**  VendorIDCity  */  
   VendorIDCity:string,
      /**  VendorIDCountry  */  
   VendorIDCountry:string,
      /**  VendorIDCurrencyCode  */  
   VendorIDCurrencyCode:string,
      /**  VendorIDDefaultFOB  */  
   VendorIDDefaultFOB:string,
      /**  VendorIDName  */  
   VendorIDName:string,
      /**  VendorIDState  */  
   VendorIDState:string,
      /**  VendorIDTermsCode  */  
   VendorIDTermsCode:string,
      /**  VendorIDVendorID  */  
   VendorIDVendorID:string,
      /**  VendorIDZIP  */  
   VendorIDZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNoListTableset{
   SerialNoList:Erp_Tablesets_SerialNoListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SerialNoRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   SerialNumber:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Job number.  The job number that this item is linked to.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   MtlSeq:number,
      /**  Packing Slip.  The Packing slip number that this serial numbered item shiped on.  */  
   PackNum:number,
      /**  The packing slip line that this serial numbered item shipped on.  */  
   PackLine:number,
      /**  Indicates that this serial number has been voided.  */  
   Voided:boolean,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   Scrapped:boolean,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackSlipLine:number,
      /**  if false idicates that this record can be used.  */  
   Selected:boolean,
      /**  The status of this serial numbered item prior to its current status.  */  
   PrevSNStatus:string,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   SNPrefix:string,
      /**  Format of the Base number.  */  
   SNFormat:string,
      /**  Information about serail number formatting.  */  
   SNBaseStructure:string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   SNBaseNumber:string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   ScrapReasonCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   SNReference:string,
      /**  Return Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line # of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA receipt  */  
   RMAReceipt:number,
      /**  DMR Number to identify the DMR record.  */  
   DMRNum:number,
      /**  The date that this serial numbered was created.  */  
   CreateDate:string,
      /**  DMR action number.  */  
   DMRActionNum:number,
      /**  Indicates that this item has failed inspection.  */  
   FailSelect:boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   LineDetailNum:number,
      /**  Used to tie back to the related RMADisp record.  */  
   RMADisp:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfNum:number,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The latest of the 3 warranty expiration dates  */  
   WarrExpiration:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Created By  */  
   CreatedBy:string,
      /**  Modified By  */  
   ModifiedBy:string,
      /**  Modification Date  */  
   ModifiedDate:string,
      /**  Modification Time  */  
   ModifiedTime:number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   ShippedFrom:string,
      /**  Added at shipment  */  
   TranAdd:boolean,
      /**  Used to assign/relate the serial number with a non-document type of transaction, such as inventory issue. Only has a value during the transaction entry process, once the transaction is update this field is set back to zero.  */  
   TempTranID:number,
      /**  Transfer Order packing slip.  */  
   TFPackNum:number,
      /**  Transfer Order packing slip Line.  */  
   TFPackLine:number,
      /**  Related (OrderHed) Sales Order number  */  
   OrderNum:number,
      /**  Related (OrderDtl) sales order line number  */  
   OrderLine:number,
      /**  related (OrderRel) order release number  */  
   OrderRelNum:number,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   FullyMatched:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   SNMask:string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   AddedByMatching:boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   SubConOprSeq:number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborHedSeq:number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborDtlSeq:number,
      /**  Indicates which Site?s SNFormat data was used to generate this serial number.  */  
   CreatedInPlant:string,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   LastLbrOprSeq:number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Cross Reference Part Type  */  
   XRefPartType:string,
      /**  Cross Reference Part Number  */  
   XRefPartNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Next Labor Operation Sequence  */  
   NextLbrAssySeq:number,
      /**  Next Labor Assembly Sequence  */  
   NextLbrOprSeq:number,
      /**  Latitude of Mobile FS Asset  */  
   Latitude:number,
      /**  Longitude of Mobile FS Asset  */  
   Longitude:number,
      /**  Altitude of Mobile FS Asset  */  
   Altitude:number,
      /**  Class Code Entry Field  */  
   FSAssetClassCode:string,
      /**  Field Service Level Agreement Text  */  
   FSServiceLevelAgreement:string,
      /**  Accuracy  */  
   Accuracy:number,
      /**  MeterReading  */  
   MeterReading:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  One time shipto flag  */  
   OTS:boolean,
      /**  OTS Address 1  */  
   OTSAddress1:string,
      /**  OTS Address 2  */  
   OTSAddress2:string,
      /**  OTS Address 3  */  
   OTSAddress3:string,
      /**  OTS City  */  
   OTSCity:string,
      /**  OTS Contact  */  
   OTSContact:string,
      /**  OTS Country Number  */  
   OTSCountryNum:number,
      /**  OTS Country Number  */  
   OTSCustSaved:boolean,
      /**  One Time fax number  */  
   OTSFaxNum:string,
      /**  OTS Name  */  
   OTSName:string,
      /**  OTS Phone Number  */  
   OTSPhoneNum:string,
      /**  OTS Resale ID  */  
   OTSResaleID:string,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  OTS Ship To Num  */  
   OTSShipToNum:string,
      /**  OTS State  */  
   OTSState:string,
      /**  OTS Tax Region Code  */  
   OTSTaxRegionCode:string,
      /**  OTS Zip  */  
   OTSZip:string,
      /**  PriorJobNum  */  
   PriorJobNum:string,
      /**  PriorAssemblySeq  */  
   PriorAssemblySeq:number,
      /**  PriorMtlSeq  */  
   PriorMtlSeq:number,
      /**  PriorPartNum  */  
   PriorPartNum:string,
      /**  PCID  */  
   PCID:string,
      /**  Misc Shipment Pack Num if related to a misc shipment  */  
   MscPackNum:number,
      /**  Misc Shipment Pack Line if related to a Misc Shipment  */  
   MscPackLine:number,
      /**  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AssetNum:string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AdditionNum:number,
      /**  DisposalNum  */  
   DisposalNum:number,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Related (TFOrdHed) Transfer Order number  */  
   TFOrdNum:string,
      /**  Related (TFOrdLine) Transfer Order Line number  */  
   TFOrdLine:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   AllowOTS:boolean,
      /**  Customer ID  */  
   CustID:string,
      /**  CustIDBTName  */  
   CustIDBTName:string,
      /**  CustIDCustID  */  
   CustIDCustID:string,
      /**  CustIDName  */  
   CustIDName:string,
   OTSSaved:boolean,
      /**  Scrap reason code description  */  
   ScrapReasonCodeDesc:string,
      /**  Shipt To Customer ID  */  
   ShipToCustID:string,
   ShipToName:string,
      /**  INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED  */  
   SNStatusTrans:string,
      /**  Source of transaction  */  
   TransactionSource:string,
      /**  Vendor ID  */  
   VendorID:string,
      /**  VendorIDAddress1  */  
   VendorIDAddress1:string,
      /**  VendorIDAddress2  */  
   VendorIDAddress2:string,
      /**  VendorIDAddress3  */  
   VendorIDAddress3:string,
      /**  VendorIDCity  */  
   VendorIDCity:string,
      /**  VendorIDCountry  */  
   VendorIDCountry:string,
      /**  VendorIDCurrencyCode  */  
   VendorIDCurrencyCode:string,
      /**  VendorIDDefaultFOB  */  
   VendorIDDefaultFOB:string,
      /**  VendorIDName  */  
   VendorIDName:string,
      /**  VendorIDState  */  
   VendorIDState:string,
      /**  VendorIDTermsCode  */  
   VendorIDTermsCode:string,
      /**  VendorIDVendorID  */  
   VendorIDVendorID:string,
      /**  VendorIDZIP  */  
   VendorIDZIP:string,
      /**  Displays formatted full from ship address. Only for information cannot be modified  */  
   FullFromShipToAddr:string,
      /**  Displays formatted full to ship address. Only for information cannot be modified  */  
   FullToShipToAddr:string,
      /**  External field to define the Customer to which we want to transfer the serial number  */  
   ToCustID:string,
      /**  External field to define the Customer to which we want to transfer the serial number  */  
   ToCustNum:number,
      /**  External field to define the Ship to ID,  to which we want to transfer the serial number  */  
   ToShipToNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CustNumInactive:boolean,
   CustNumBTName:string,
   CustNumAllowShipTo3:boolean,
   CustNumName:string,
   CustNumCustID:string,
   DMRNumPartDescription:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   FSAssetClassCodeFSAssetClassDesc:string,
   MtlSeqDescription:string,
   MtlSeqSalvageDescription:string,
   NonConfNumDescription:string,
   OTSCntryISOCode:string,
   OTSCntryDescription:string,
   OTSCntryEUMember:boolean,
   PackNumShipStatus:string,
   PartNumAttrClassID:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PurPointAddress1:string,
   PurPointAddress3:string,
   PurPointAddress2:string,
   PurPointCountry:string,
   PurPointZip:string,
   PurPointCity:string,
   PurPointState:string,
   PurPointName:string,
   PurPointPrimPCon:number,
   RMALineLineDesc:string,
   ScrapReasonCodeDescription:string,
   SerialMaskMaskType:number,
   SerialMaskDescription:string,
   ShipToCustName:string,
   ShipToCustNumInactive:boolean,
   ShipToNumInactive:boolean,
   TaxRegionCodeDescription:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumName:string,
   VendorNumAddress1:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress3:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNoTableset{
   SerialNo:Erp_Tablesets_SerialNoRow[],
   SerialNoAttch:Erp_Tablesets_SerialNoAttchRow[],
   SerialNoCondition:Erp_Tablesets_SerialNoConditionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtSerialNoTableset{
   SerialNo:Erp_Tablesets_SerialNoRow[],
   SerialNoAttch:Erp_Tablesets_SerialNoAttchRow[],
   SerialNoCondition:Erp_Tablesets_SerialNoConditionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
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
      @param ds
   */  
export interface FormatOTSAddress_input{
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface FormatOTSAddress_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param partNum
      @param serialNumber
   */  
export interface GetByID_input{
   partNum:string,
   serialNumber:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
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
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  Where clause for SerialNo table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSerialNo
      @param pageSize
      @param absolutePage
   */  
export interface GetListForOperation_input{
      /**  Whereclause for SNList  */  
   whereClauseSerialNo:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListForOperation_output{
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param reassignedFromJob
   */  
export interface GetListInclReassigned_input{
      /**  Where clause for SerialNo table.  */  
   whereClause:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
      /**  Includes reassigned serial numbers from this job  */  
   reassignedFromJob:string,
}

export interface GetListInclReassigned_output{
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSerialNo
      @param pageSize
      @param absolutePage
      @param contractNum
      @param contractLine
   */  
export interface GetListServiceCall_input{
      /**  Whereclause for SNList  */  
   whereClauseSerialNo:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
      /**  Contract Num.  */  
   contractNum:number,
      /**  Contract Line.  */  
   contractLine:number,
}

export interface GetListServiceCall_output{
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param serialNumber
   */  
export interface GetNewSerialNoAttch_input{
   ds:Erp_Tablesets_SerialNoTableset[],
   partNum:string,
   serialNumber:string,
}

export interface GetNewSerialNoAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
      @param serialNumber
   */  
export interface GetNewSerialNoCondition_input{
   ds:Erp_Tablesets_SerialNoTableset[],
   partNum:string,
   serialNumber:string,
}

export interface GetNewSerialNoCondition_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewSerialNo_input{
   ds:Erp_Tablesets_SerialNoTableset[],
   partNum:string,
}

export interface GetNewSerialNo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowId_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowId_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
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
      @param paramPCID
   */  
export interface GetRowsPerPCID_input{
      /**  Unique identifier of the Plant, if it's an empty string it will search for all Plants  */  
   paramPCID:string,
}

export interface GetRowsPerPCID_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
}

   /** Required : 
      @param partNum
      @param SNInWIP
      @param SNRejAdj
      @param SNShipped
      @param SNConsumed
      @param SNAsset
      @param SNWhsePlant
   */  
export interface GetRowsPerPlantKinetic_input{
   partNum:string,
   SNInWIP:boolean,
   SNRejAdj:boolean,
   SNShipped:boolean,
   SNConsumed:boolean,
   SNAsset:boolean,
   SNWhsePlant:string,
}

export interface GetRowsPerPlantKinetic_output{
   returnObj:Erp_Tablesets_AltSerialNoTableset[],
}

   /** Required : 
      @param paramWhereClause
      @param paramPlant
   */  
export interface GetRowsPerPlant_input{
      /**  String Representing the WHERE Clause, Company = cur-comp is already assumed  */  
   paramWhereClause:string,
      /**  Unique identifier of the Plant, if it's an empty string it will search for all Plants  */  
   paramPlant:string,
}

export interface GetRowsPerPlant_output{
   returnObj:Erp_Tablesets_AltSerialNoTableset[],
}

   /** Required : 
      @param whereClauseSerialNo
      @param pageSize
      @param absolutePage
      @param contractNum
      @param contractLine
   */  
export interface GetRowsServiceCall_input{
      /**  Whereclause for SN  */  
   whereClauseSerialNo:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
      /**  Contract Num  */  
   contractNum:number,
      /**  Contract Line  */  
   contractLine:number,
}

export interface GetRowsServiceCall_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSerialNo
      @param whereClauseSerialNoAttch
      @param whereClauseSerialNoCondition
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSerialNo:string,
   whereClauseSerialNoAttch:string,
   whereClauseSerialNoCondition:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetSerialNumbersNotCompleted_input{
      /**  Where clause for SNList  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetSerialNumbersNotCompleted_output{
   returnObj:Erp_Tablesets_SerialNoListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPackNum
      @param ipPackLine
   */  
export interface GetSerialsForCustShipTracker_input{
      /**  Packnum  */  
   ipPackNum:number,
      /**  PackLine  */  
   ipPackLine:number,
}

export interface GetSerialsForCustShipTracker_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
}

   /** Required : 
      @param ipCompany
      @param ipJobNum
   */  
export interface GetSerialsForJobTracker_input{
      /**  Company  */  
   ipCompany:string,
      /**  Job Number  */  
   ipJobNum:string,
}

export interface GetSerialsForJobTracker_output{
   returnObj:Erp_Tablesets_SerialNoTableset[],
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
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

export interface PlantSerialTracking_output{
parameters : {
      /**  output parameters  */  
   plantTracking:boolean,
}
}

   /** Required : 
      @param serialNumber
   */  
export interface SerialNumberExists_input{
      /**  Serial Number  */  
   serialNumber:string,
}

export interface SerialNumberExists_output{
parameters : {
      /**  output parameters  */  
   snExists:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtSerialNoTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtSerialNoTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SerialNoTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_SerialNoTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNoTableset[],
   opMessage:string,
}
}


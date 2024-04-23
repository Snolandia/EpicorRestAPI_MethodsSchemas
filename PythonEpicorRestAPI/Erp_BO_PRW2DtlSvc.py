import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PRW2DtlSvc
# Description: Payroll W2 detail file.  Each record in this file represents one W2.
IMPORTANT NOTE: THE REPORT NAME FOR W2EXPORT SHOULD BE 'W2REPORT'.
IT IS A IRS REQUIREMENT.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PRW2Dtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRW2Dtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRW2Dtls
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls",headers=creds) as resp:
           return await resp.json()

async def post_PRW2Dtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRW2Dtls_Company_TaxYear_ControlNum(Company, TaxYear, ControlNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRW2Dtl item
   Description: Calls GetByID to retrieve the PRW2Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRW2Dtls_Company_TaxYear_ControlNum(Company, TaxYear, ControlNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRW2Dtl for the service
   Description: Calls UpdateExt to update PRW2Dtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRW2Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRW2Dtls_Company_TaxYear_ControlNum(Company, TaxYear, ControlNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRW2Dtl item
   Description: Call UpdateExt to delete PRW2Dtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRW2Dtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRW2Dtls_Company_TaxYear_ControlNum_PRW2DtlBoxs(Company, TaxYear, ControlNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRW2DtlBoxs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRW2DtlBoxs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")/PRW2DtlBoxs",headers=creds) as resp:
           return await resp.json()

async def get_PRW2Dtls_Company_TaxYear_ControlNum_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company, TaxYear, ControlNum, BoxType, BoxSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRW2DtlBox item
   Description: Calls GetByID to retrieve the PRW2DtlBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2DtlBox1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param BoxType: Desc: BoxType   Required: True   Allow empty value : True
      :param BoxSeq: Desc: BoxSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRW2DtlBoxs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRW2DtlBoxs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRW2DtlBoxs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs",headers=creds) as resp:
           return await resp.json()

async def post_PRW2DtlBoxs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRW2DtlBoxs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company, TaxYear, ControlNum, BoxType, BoxSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRW2DtlBox item
   Description: Calls GetByID to retrieve the PRW2DtlBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2DtlBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param BoxType: Desc: BoxType   Required: True   Allow empty value : True
      :param BoxSeq: Desc: BoxSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company, TaxYear, ControlNum, BoxType, BoxSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRW2DtlBox for the service
   Description: Calls UpdateExt to update PRW2DtlBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRW2DtlBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param BoxType: Desc: BoxType   Required: True   Allow empty value : True
      :param BoxSeq: Desc: BoxSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company, TaxYear, ControlNum, BoxType, BoxSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRW2DtlBox item
   Description: Call UpdateExt to delete PRW2DtlBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRW2DtlBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param ControlNum: Desc: ControlNum   Required: True
      :param BoxType: Desc: BoxType   Required: True   Allow empty value : True
      :param BoxSeq: Desc: BoxSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRW2Dtl, whereClausePRW2DtlBox, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRW2Dtl=" + whereClausePRW2Dtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRW2DtlBox=" + whereClausePRW2DtlBox
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxYear, controlNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taxYear=" + taxYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "controlNum=" + controlNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckPRW2DtlExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPRW2DtlExists
   Description: Checks if a W2 form exists for the year.
   OperationID: CheckPRW2DtlExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRW2DtlExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRW2DtlExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPRChecksExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPRChecksExist
   Description: Checks if there are posted payroll checks for the entered year
   OperationID: CheckPRChecksExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRChecksExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRChecksExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUser(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUser
   Description: Validate if the user has the rights to proceed.
   OperationID: ValidateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeletePRW2Dtls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePRW2Dtls
   Description: This procedure deletes the PRW2Dtl records from the database.
   OperationID: DeletePRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePRW2Dtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePRW2Dtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportPRW2Dtls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportPRW2Dtls
   Description: This procedure takes the pin code number and tax year as input parameters
and returns the PRW2DtlExportDataSet.  The UI person has to read the records
in the data set and export it in the LineNum order.  It is very important
that the export order be in the line number ascending order.
   OperationID: ExportPRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportPRW2Dtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportPRW2Dtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportPRW2DtlsFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportPRW2DtlsFile
   OperationID: ExportPRW2DtlsFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportPRW2DtlsFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportPRW2DtlsFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFile
   Description: Deletes file from UserData storage
   OperationID: DeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableControlNums(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableControlNums
   Description: Returns the available controlnums for an employee on w2 file
takes taxyear and empid as input parameters
   OperationID: GetAvailableControlNums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableControlNums_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableControlNums_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmployeeAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmployeeAddress
   Description: Gets Employee Adress
   OperationID: GetEmployeeAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmployeeAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployeeAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmployerAddress(epicorHeaders = None):
   """  
   Summary: Invoke method GetEmployerAddress
   Description: Gets Employer Adress
   OperationID: GetEmployerAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployerAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetEmployerEIN(epicorHeaders = None):
   """  
   Summary: Invoke method GetEmployerEIN
   Description: Gets Employer FIN
   OperationID: GetEmployerEIN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployerEIN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LeaveTaxYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveTaxYear
   Description: This procedrue must be called on leave of TaxYear field.
   OperationID: LeaveTaxYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveTaxYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveTaxYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRW2Dtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRW2Dtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRW2Dtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRW2Dtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRW2Dtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRW2DtlBox(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRW2DtlBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRW2DtlBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRW2DtlBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRW2DtlBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRW2DtlBoxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRW2DtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRW2DtlRow] = obj["value"]
      pass

class Erp_Tablesets_PRW2DtlBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaxYear:int = obj["TaxYear"]
      """  TaxYear  """  
      self.ControlNum:int = obj["ControlNum"]
      """  ControlNum  """  
      self.BoxType:str = obj["BoxType"]
      """  BoxType  """  
      self.BoxSeq:int = obj["BoxSeq"]
      """  BoxSeq  """  
      self.BoxCode:str = obj["BoxCode"]
      """  BoxCode  """  
      self.BoxAmount:int = obj["BoxAmount"]
      """  BoxAmount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Identifies the tax year of this W2 record. Used as a component in the primary index.  """  
      self.ControlNum:int = obj["ControlNum"]
      """  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.VoidW2:bool = obj["VoidW2"]
      """  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  """  
      self.FitWages:int = obj["FitWages"]
      """  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  """  
      self.FitTax:int = obj["FitTax"]
      """  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  """  
      self.SSWages:int = obj["SSWages"]
      """  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  """  
      self.SSTax:int = obj["SSTax"]
      """  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  """  
      self.SSTips:int = obj["SSTips"]
      """  Social Security Tips  """  
      self.AllocTips:int = obj["AllocTips"]
      """  Allocation Tips  """  
      self.MediWages:int = obj["MediWages"]
      """  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  """  
      self.MediTax:int = obj["MediTax"]
      """  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  """  
      self.AdvanceEIC:int = obj["AdvanceEIC"]
      """  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  """  
      self.DependCare:int = obj["DependCare"]
      """  Dependent care benefits. Not generated by system.  """  
      self.NQPlan:int = obj["NQPlan"]
      """  amount of Nonqualified plans. Not generated by system.  """  
      self.FringeBenefits:int = obj["FringeBenefits"]
      """  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  """  
      self.Statutory:bool = obj["Statutory"]
      """  Statutory Employee  """  
      self.Deceased:bool = obj["Deceased"]
      """  Deceased  """  
      self.Pension:bool = obj["Pension"]
      """  Pension Plan  """  
      self.LegalRep:bool = obj["LegalRep"]
      """  Legal Representation  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  New field added for 5.2.  Indicates a reirement plan.  """  
      self.HouseHold:bool = obj["HouseHold"]
      """  Household Employee  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay.  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Deferred Compensation  """  
      self.State1TaxTblID:str = obj["State1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State1Wages:int = obj["State1Wages"]
      """  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State1Tax:int = obj["State1Tax"]
      """  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State2TaxTblID:str = obj["State2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State2Wages:int = obj["State2Wages"]
      """  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  """  
      self.State2Tax:int = obj["State2Tax"]
      """  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  """  
      self.Local1TaxTblID:str = obj["Local1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  """  
      self.Local1Wages:int = obj["Local1Wages"]
      """  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local1Tax:int = obj["Local1Tax"]
      """  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local2TaxTblID:str = obj["Local2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  """  
      self.Local2Wages:int = obj["Local2Wages"]
      """  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  """  
      self.Local2Tax:int = obj["Local2Tax"]
      """  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  """  
      self.MiscAmt1:int = obj["MiscAmt1"]
      """  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  """  
      self.MiscAmt2:int = obj["MiscAmt2"]
      """  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt3:int = obj["MiscAmt3"]
      """  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt4:int = obj["MiscAmt4"]
      """  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  """  
      self.MiscCode1:str = obj["MiscCode1"]
      """  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  """  
      self.MiscCode2:str = obj["MiscCode2"]
      """  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode3:str = obj["MiscCode3"]
      """  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode4:str = obj["MiscCode4"]
      """  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  """  
      self.OtherAmt1:int = obj["OtherAmt1"]
      """  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  """  
      self.OtherAmt2:int = obj["OtherAmt2"]
      """  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherAmt3:int = obj["OtherAmt3"]
      """  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherCode1:str = obj["OtherCode1"]
      """  Associated Code for OtherAmt1  """  
      self.OtherCode2:str = obj["OtherCode2"]
      """  Associated Code for OtherAmt2  """  
      self.OtherCode3:str = obj["OtherCode3"]
      """  Associated Code for OtherAmt3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.State1TaxDesc:str = obj["State1TaxDesc"]
      """  State1TaxDesc  """  
      self.State2TaxDesc:str = obj["State2TaxDesc"]
      """  State2TaxDesc  """  
      self.EmpID:str = obj["EmpID"]
      self.SSNum:str = obj["SSNum"]
      self.StateTaxID1:str = obj["StateTaxID1"]
      self.StateTaxID2:str = obj["StateTaxID2"]
      self.EmpName:str = obj["EmpName"]
      self.EmployeeAddress:str = obj["EmployeeAddress"]
      self.FirstName:str = obj["FirstName"]
      self.MiddleInitial:str = obj["MiddleInitial"]
      self.LastName:str = obj["LastName"]
      self.tmpMiscCode1:str = obj["tmpMiscCode1"]
      self.tmpMiscCode2:str = obj["tmpMiscCode2"]
      self.tmpMiscCode3:str = obj["tmpMiscCode3"]
      self.tmpMiscCode4:str = obj["tmpMiscCode4"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      """  Last name of employee  """  
      self.EmpLinkName:str = obj["EmpLinkName"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      """  First name of employee.  """  
      self.vrEmpLinkLastName:str = obj["vrEmpLinkLastName"]
      """  Last name of employee  """  
      self.vrEmpLinkName:str = obj["vrEmpLinkName"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.vrEmpLinkFirstName:str = obj["vrEmpLinkFirstName"]
      """  First name of employee.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Identifies the tax year of this W2 record. Used as a component in the primary index.  """  
      self.ControlNum:int = obj["ControlNum"]
      """  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.VoidW2:bool = obj["VoidW2"]
      """  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  """  
      self.FitWages:int = obj["FitWages"]
      """  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  """  
      self.FitTax:int = obj["FitTax"]
      """  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  """  
      self.SSWages:int = obj["SSWages"]
      """  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  """  
      self.SSTax:int = obj["SSTax"]
      """  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  """  
      self.SSTips:int = obj["SSTips"]
      """  Social Security Tips  """  
      self.AllocTips:int = obj["AllocTips"]
      """  Allocation Tips  """  
      self.MediWages:int = obj["MediWages"]
      """  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  """  
      self.MediTax:int = obj["MediTax"]
      """  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  """  
      self.AdvanceEIC:int = obj["AdvanceEIC"]
      """  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  """  
      self.DependCare:int = obj["DependCare"]
      """  Dependent care benefits. Not generated by system.  """  
      self.NQPlan:int = obj["NQPlan"]
      """  amount of Nonqualified plans. Not generated by system.  """  
      self.FringeBenefits:int = obj["FringeBenefits"]
      """  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  """  
      self.Statutory:bool = obj["Statutory"]
      """  Statutory Employee  """  
      self.Deceased:bool = obj["Deceased"]
      """  Deceased  """  
      self.Pension:bool = obj["Pension"]
      """  Pension Plan  """  
      self.LegalRep:bool = obj["LegalRep"]
      """  Legal Representation  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  New field added for 5.2.  Indicates a reirement plan.  """  
      self.HouseHold:bool = obj["HouseHold"]
      """  Household Employee  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay.  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Deferred Compensation  """  
      self.State1TaxTblID:str = obj["State1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State1Wages:int = obj["State1Wages"]
      """  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State1Tax:int = obj["State1Tax"]
      """  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State2TaxTblID:str = obj["State2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State2Wages:int = obj["State2Wages"]
      """  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  """  
      self.State2Tax:int = obj["State2Tax"]
      """  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  """  
      self.Local1TaxTblID:str = obj["Local1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  """  
      self.Local1Wages:int = obj["Local1Wages"]
      """  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local1Tax:int = obj["Local1Tax"]
      """  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local2TaxTblID:str = obj["Local2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  """  
      self.Local2Wages:int = obj["Local2Wages"]
      """  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  """  
      self.Local2Tax:int = obj["Local2Tax"]
      """  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  """  
      self.MiscAmt1:int = obj["MiscAmt1"]
      """  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  """  
      self.MiscAmt2:int = obj["MiscAmt2"]
      """  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt3:int = obj["MiscAmt3"]
      """  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt4:int = obj["MiscAmt4"]
      """  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  """  
      self.MiscCode1:str = obj["MiscCode1"]
      """  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  """  
      self.MiscCode2:str = obj["MiscCode2"]
      """  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode3:str = obj["MiscCode3"]
      """  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode4:str = obj["MiscCode4"]
      """  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  """  
      self.OtherAmt1:int = obj["OtherAmt1"]
      """  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  """  
      self.OtherAmt2:int = obj["OtherAmt2"]
      """  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherAmt3:int = obj["OtherAmt3"]
      """  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherCode1:str = obj["OtherCode1"]
      """  Associated Code for OtherAmt1  """  
      self.OtherCode2:str = obj["OtherCode2"]
      """  Associated Code for OtherAmt2  """  
      self.OtherCode3:str = obj["OtherCode3"]
      """  Associated Code for OtherAmt3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.State1TaxDesc:str = obj["State1TaxDesc"]
      """  State1TaxDesc  """  
      self.State2TaxDesc:str = obj["State2TaxDesc"]
      """  State2TaxDesc  """  
      self.SmtrInfo:str = obj["SmtrInfo"]
      """  SmtrInfo  """  
      self.ContactInfo:str = obj["ContactInfo"]
      """  ContactInfo  """  
      self.PrefNotiCode:str = obj["PrefNotiCode"]
      """  PrefNotiCode  """  
      self.ContactEMail:str = obj["ContactEMail"]
      """  Contact Email Address  """  
      self.ContactExt:str = obj["ContactExt"]
      """  Phone Extension  """  
      self.ContactFax:str = obj["ContactFax"]
      self.ContactName:str = obj["ContactName"]
      """  Contact Name  """  
      self.ContactPhone:str = obj["ContactPhone"]
      self.EmployeeAddress:str = obj["EmployeeAddress"]
      self.EmpName:str = obj["EmpName"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.MiddleInitial:str = obj["MiddleInitial"]
      self.PrefMethNotificationCode:int = obj["PrefMethNotificationCode"]
      """   Preferred method of notification code...

1. Email/Internet
2. U.S. Postal Service  """  
      self.SmtrCity:str = obj["SmtrCity"]
      self.SmtrDeliveryAddr:str = obj["SmtrDeliveryAddr"]
      """  Submitter Delivery Address  """  
      self.SmtrLocation:str = obj["SmtrLocation"]
      """  Room Number, Suite Number etc...  """  
      self.SmtrName:str = obj["SmtrName"]
      """  Submitter Name  """  
      self.SmtrState:str = obj["SmtrState"]
      self.SmtrZip:str = obj["SmtrZip"]
      self.SmtrZipExt:str = obj["SmtrZipExt"]
      self.StateTaxID2:str = obj["StateTaxID2"]
      self.EmpID:str = obj["EmpID"]
      self.SSNum:str = obj["SSNum"]
      self.StateTaxID1:str = obj["StateTaxID1"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkClassID:str = obj["EmpLinkClassID"]
      self.vrEmpLinkName:str = obj["vrEmpLinkName"]
      self.vrEmpLinkLastName:str = obj["vrEmpLinkLastName"]
      self.vrEmpLinkFirstName:str = obj["vrEmpLinkFirstName"]
      self.vrEmpLinkClassID:str = obj["vrEmpLinkClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckPRChecksExist_input:
   """ Required : 
   InTaxYear
   """  
   def __init__(self, obj):
      self.InTaxYear:int = obj["InTaxYear"]
      """  Tax Year  """  
      pass

class CheckPRChecksExist_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPRW2DtlExists_input:
   """ Required : 
   InTaxYear
   """  
   def __init__(self, obj):
      self.InTaxYear:int = obj["InTaxYear"]
      """  The tax year  """  
      pass

class CheckPRW2DtlExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DataExists:bool = obj["DataExists"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   taxYear
   controlNum
   """  
   def __init__(self, obj):
      self.taxYear:int = obj["taxYear"]
      self.controlNum:int = obj["controlNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteFile_input:
   """ Required : 
   filename
   """  
   def __init__(self, obj):
      self.filename:str = obj["filename"]
      """  File name of a file in UserData folder we need to delete  """  
      pass

class DeleteFile_output:
   def __init__(self, obj):
      pass

class DeletePRW2Dtls_input:
   """ Required : 
   TaxYrFill
   ds
   """  
   def __init__(self, obj):
      self.TaxYrFill:int = obj["TaxYrFill"]
      """  Tax Year  """  
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

class DeletePRW2Dtls_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PRW2DtlBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaxYear:int = obj["TaxYear"]
      """  TaxYear  """  
      self.ControlNum:int = obj["ControlNum"]
      """  ControlNum  """  
      self.BoxType:str = obj["BoxType"]
      """  BoxType  """  
      self.BoxSeq:int = obj["BoxSeq"]
      """  BoxSeq  """  
      self.BoxCode:str = obj["BoxCode"]
      """  BoxCode  """  
      self.BoxAmount:int = obj["BoxAmount"]
      """  BoxAmount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlExportRow:
   def __init__(self, obj):
      self.ExportLine:str = obj["ExportLine"]
      self.LineNum:int = obj["LineNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlExportTableset:
   def __init__(self, obj):
      self.PRW2DtlExport:list[Erp_Tablesets_PRW2DtlExportRow] = obj["PRW2DtlExport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRW2DtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Identifies the tax year of this W2 record. Used as a component in the primary index.  """  
      self.ControlNum:int = obj["ControlNum"]
      """  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.VoidW2:bool = obj["VoidW2"]
      """  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  """  
      self.FitWages:int = obj["FitWages"]
      """  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  """  
      self.FitTax:int = obj["FitTax"]
      """  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  """  
      self.SSWages:int = obj["SSWages"]
      """  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  """  
      self.SSTax:int = obj["SSTax"]
      """  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  """  
      self.SSTips:int = obj["SSTips"]
      """  Social Security Tips  """  
      self.AllocTips:int = obj["AllocTips"]
      """  Allocation Tips  """  
      self.MediWages:int = obj["MediWages"]
      """  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  """  
      self.MediTax:int = obj["MediTax"]
      """  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  """  
      self.AdvanceEIC:int = obj["AdvanceEIC"]
      """  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  """  
      self.DependCare:int = obj["DependCare"]
      """  Dependent care benefits. Not generated by system.  """  
      self.NQPlan:int = obj["NQPlan"]
      """  amount of Nonqualified plans. Not generated by system.  """  
      self.FringeBenefits:int = obj["FringeBenefits"]
      """  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  """  
      self.Statutory:bool = obj["Statutory"]
      """  Statutory Employee  """  
      self.Deceased:bool = obj["Deceased"]
      """  Deceased  """  
      self.Pension:bool = obj["Pension"]
      """  Pension Plan  """  
      self.LegalRep:bool = obj["LegalRep"]
      """  Legal Representation  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  New field added for 5.2.  Indicates a reirement plan.  """  
      self.HouseHold:bool = obj["HouseHold"]
      """  Household Employee  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay.  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Deferred Compensation  """  
      self.State1TaxTblID:str = obj["State1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State1Wages:int = obj["State1Wages"]
      """  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State1Tax:int = obj["State1Tax"]
      """  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State2TaxTblID:str = obj["State2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State2Wages:int = obj["State2Wages"]
      """  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  """  
      self.State2Tax:int = obj["State2Tax"]
      """  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  """  
      self.Local1TaxTblID:str = obj["Local1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  """  
      self.Local1Wages:int = obj["Local1Wages"]
      """  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local1Tax:int = obj["Local1Tax"]
      """  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local2TaxTblID:str = obj["Local2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  """  
      self.Local2Wages:int = obj["Local2Wages"]
      """  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  """  
      self.Local2Tax:int = obj["Local2Tax"]
      """  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  """  
      self.MiscAmt1:int = obj["MiscAmt1"]
      """  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  """  
      self.MiscAmt2:int = obj["MiscAmt2"]
      """  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt3:int = obj["MiscAmt3"]
      """  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt4:int = obj["MiscAmt4"]
      """  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  """  
      self.MiscCode1:str = obj["MiscCode1"]
      """  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  """  
      self.MiscCode2:str = obj["MiscCode2"]
      """  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode3:str = obj["MiscCode3"]
      """  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode4:str = obj["MiscCode4"]
      """  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  """  
      self.OtherAmt1:int = obj["OtherAmt1"]
      """  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  """  
      self.OtherAmt2:int = obj["OtherAmt2"]
      """  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherAmt3:int = obj["OtherAmt3"]
      """  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherCode1:str = obj["OtherCode1"]
      """  Associated Code for OtherAmt1  """  
      self.OtherCode2:str = obj["OtherCode2"]
      """  Associated Code for OtherAmt2  """  
      self.OtherCode3:str = obj["OtherCode3"]
      """  Associated Code for OtherAmt3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.State1TaxDesc:str = obj["State1TaxDesc"]
      """  State1TaxDesc  """  
      self.State2TaxDesc:str = obj["State2TaxDesc"]
      """  State2TaxDesc  """  
      self.EmpID:str = obj["EmpID"]
      self.SSNum:str = obj["SSNum"]
      self.StateTaxID1:str = obj["StateTaxID1"]
      self.StateTaxID2:str = obj["StateTaxID2"]
      self.EmpName:str = obj["EmpName"]
      self.EmployeeAddress:str = obj["EmployeeAddress"]
      self.FirstName:str = obj["FirstName"]
      self.MiddleInitial:str = obj["MiddleInitial"]
      self.LastName:str = obj["LastName"]
      self.tmpMiscCode1:str = obj["tmpMiscCode1"]
      self.tmpMiscCode2:str = obj["tmpMiscCode2"]
      self.tmpMiscCode3:str = obj["tmpMiscCode3"]
      self.tmpMiscCode4:str = obj["tmpMiscCode4"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      """  Last name of employee  """  
      self.EmpLinkName:str = obj["EmpLinkName"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      """  First name of employee.  """  
      self.vrEmpLinkLastName:str = obj["vrEmpLinkLastName"]
      """  Last name of employee  """  
      self.vrEmpLinkName:str = obj["vrEmpLinkName"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.vrEmpLinkFirstName:str = obj["vrEmpLinkFirstName"]
      """  First name of employee.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlListTableset:
   def __init__(self, obj):
      self.PRW2DtlList:list[Erp_Tablesets_PRW2DtlListRow] = obj["PRW2DtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRW2DtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Identifies the tax year of this W2 record. Used as a component in the primary index.  """  
      self.ControlNum:int = obj["ControlNum"]
      """  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.VoidW2:bool = obj["VoidW2"]
      """  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  """  
      self.FitWages:int = obj["FitWages"]
      """  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  """  
      self.FitTax:int = obj["FitTax"]
      """  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  """  
      self.SSWages:int = obj["SSWages"]
      """  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  """  
      self.SSTax:int = obj["SSTax"]
      """  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  """  
      self.SSTips:int = obj["SSTips"]
      """  Social Security Tips  """  
      self.AllocTips:int = obj["AllocTips"]
      """  Allocation Tips  """  
      self.MediWages:int = obj["MediWages"]
      """  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  """  
      self.MediTax:int = obj["MediTax"]
      """  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  """  
      self.AdvanceEIC:int = obj["AdvanceEIC"]
      """  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  """  
      self.DependCare:int = obj["DependCare"]
      """  Dependent care benefits. Not generated by system.  """  
      self.NQPlan:int = obj["NQPlan"]
      """  amount of Nonqualified plans. Not generated by system.  """  
      self.FringeBenefits:int = obj["FringeBenefits"]
      """  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  """  
      self.Statutory:bool = obj["Statutory"]
      """  Statutory Employee  """  
      self.Deceased:bool = obj["Deceased"]
      """  Deceased  """  
      self.Pension:bool = obj["Pension"]
      """  Pension Plan  """  
      self.LegalRep:bool = obj["LegalRep"]
      """  Legal Representation  """  
      self.RetirePlan:bool = obj["RetirePlan"]
      """  New field added for 5.2.  Indicates a reirement plan.  """  
      self.HouseHold:bool = obj["HouseHold"]
      """  Household Employee  """  
      self.ThirdPartySickPay:bool = obj["ThirdPartySickPay"]
      """  Indicates if there is third part sick pay.  """  
      self.DeferredComp:bool = obj["DeferredComp"]
      """  Deferred Compensation  """  
      self.State1TaxTblID:str = obj["State1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State1Wages:int = obj["State1Wages"]
      """  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State1Tax:int = obj["State1Tax"]
      """  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  """  
      self.State2TaxTblID:str = obj["State2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  """  
      self.State2Wages:int = obj["State2Wages"]
      """  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  """  
      self.State2Tax:int = obj["State2Tax"]
      """  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  """  
      self.Local1TaxTblID:str = obj["Local1TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  """  
      self.Local1Wages:int = obj["Local1Wages"]
      """  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local1Tax:int = obj["Local1Tax"]
      """  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  """  
      self.Local2TaxTblID:str = obj["Local2TaxTblID"]
      """  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  """  
      self.Local2Wages:int = obj["Local2Wages"]
      """  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  """  
      self.Local2Tax:int = obj["Local2Tax"]
      """  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  """  
      self.MiscAmt1:int = obj["MiscAmt1"]
      """  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  """  
      self.MiscAmt2:int = obj["MiscAmt2"]
      """  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt3:int = obj["MiscAmt3"]
      """  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  """  
      self.MiscAmt4:int = obj["MiscAmt4"]
      """  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  """  
      self.MiscCode1:str = obj["MiscCode1"]
      """  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  """  
      self.MiscCode2:str = obj["MiscCode2"]
      """  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode3:str = obj["MiscCode3"]
      """  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  """  
      self.MiscCode4:str = obj["MiscCode4"]
      """  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  """  
      self.OtherAmt1:int = obj["OtherAmt1"]
      """  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  """  
      self.OtherAmt2:int = obj["OtherAmt2"]
      """  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherAmt3:int = obj["OtherAmt3"]
      """  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  """  
      self.OtherCode1:str = obj["OtherCode1"]
      """  Associated Code for OtherAmt1  """  
      self.OtherCode2:str = obj["OtherCode2"]
      """  Associated Code for OtherAmt2  """  
      self.OtherCode3:str = obj["OtherCode3"]
      """  Associated Code for OtherAmt3  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.State1TaxDesc:str = obj["State1TaxDesc"]
      """  State1TaxDesc  """  
      self.State2TaxDesc:str = obj["State2TaxDesc"]
      """  State2TaxDesc  """  
      self.SmtrInfo:str = obj["SmtrInfo"]
      """  SmtrInfo  """  
      self.ContactInfo:str = obj["ContactInfo"]
      """  ContactInfo  """  
      self.PrefNotiCode:str = obj["PrefNotiCode"]
      """  PrefNotiCode  """  
      self.ContactEMail:str = obj["ContactEMail"]
      """  Contact Email Address  """  
      self.ContactExt:str = obj["ContactExt"]
      """  Phone Extension  """  
      self.ContactFax:str = obj["ContactFax"]
      self.ContactName:str = obj["ContactName"]
      """  Contact Name  """  
      self.ContactPhone:str = obj["ContactPhone"]
      self.EmployeeAddress:str = obj["EmployeeAddress"]
      self.EmpName:str = obj["EmpName"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.MiddleInitial:str = obj["MiddleInitial"]
      self.PrefMethNotificationCode:int = obj["PrefMethNotificationCode"]
      """   Preferred method of notification code...

1. Email/Internet
2. U.S. Postal Service  """  
      self.SmtrCity:str = obj["SmtrCity"]
      self.SmtrDeliveryAddr:str = obj["SmtrDeliveryAddr"]
      """  Submitter Delivery Address  """  
      self.SmtrLocation:str = obj["SmtrLocation"]
      """  Room Number, Suite Number etc...  """  
      self.SmtrName:str = obj["SmtrName"]
      """  Submitter Name  """  
      self.SmtrState:str = obj["SmtrState"]
      self.SmtrZip:str = obj["SmtrZip"]
      self.SmtrZipExt:str = obj["SmtrZipExt"]
      self.StateTaxID2:str = obj["StateTaxID2"]
      self.EmpID:str = obj["EmpID"]
      self.SSNum:str = obj["SSNum"]
      self.StateTaxID1:str = obj["StateTaxID1"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkClassID:str = obj["EmpLinkClassID"]
      self.vrEmpLinkName:str = obj["vrEmpLinkName"]
      self.vrEmpLinkLastName:str = obj["vrEmpLinkLastName"]
      self.vrEmpLinkFirstName:str = obj["vrEmpLinkFirstName"]
      self.vrEmpLinkClassID:str = obj["vrEmpLinkClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRW2DtlTableset:
   def __init__(self, obj):
      self.PRW2Dtl:list[Erp_Tablesets_PRW2DtlRow] = obj["PRW2Dtl"]
      self.PRW2DtlBox:list[Erp_Tablesets_PRW2DtlBoxRow] = obj["PRW2DtlBox"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPRW2DtlTableset:
   def __init__(self, obj):
      self.PRW2Dtl:list[Erp_Tablesets_PRW2DtlRow] = obj["PRW2Dtl"]
      self.PRW2DtlBox:list[Erp_Tablesets_PRW2DtlBoxRow] = obj["PRW2DtlBox"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportPRW2DtlsFile_input:
   """ Required : 
   PinNum
   TaxYrFill
   """  
   def __init__(self, obj):
      self.PinNum:str = obj["PinNum"]
      self.TaxYrFill:int = obj["TaxYrFill"]
      pass

class ExportPRW2DtlsFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExportPRW2Dtls_input:
   """ Required : 
   PinNum
   TaxYrFill
   """  
   def __init__(self, obj):
      self.PinNum:str = obj["PinNum"]
      """  Pin code Number  """  
      self.TaxYrFill:int = obj["TaxYrFill"]
      """  Tax Year  """  
      pass

class ExportPRW2Dtls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlExportTableset] = obj["returnObj"]
      pass

class GetAvailableControlNums_input:
   """ Required : 
   ipEmpID
   ipTaxYear
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  The Employee ID to get the controlnums  """  
      self.ipTaxYear:int = obj["ipTaxYear"]
      """  The TaxYearto get the controlnums  """  
      pass

class GetAvailableControlNums_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opControlNums:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   taxYear
   controlNum
   """  
   def __init__(self, obj):
      self.taxYear:int = obj["taxYear"]
      self.controlNum:int = obj["controlNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlTableset] = obj["returnObj"]
      pass

class GetEmployeeAddress_input:
   """ Required : 
   EmpID
   """  
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      pass

class GetEmployeeAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.EmployeeAddress:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetEmployerAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.EmployerAddress:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetEmployerEIN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oEIN:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPRW2DtlBox_input:
   """ Required : 
   ds
   taxYear
   controlNum
   boxType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      self.taxYear:int = obj["taxYear"]
      self.controlNum:int = obj["controlNum"]
      self.boxType:str = obj["boxType"]
      pass

class GetNewPRW2DtlBox_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRW2Dtl_input:
   """ Required : 
   ds
   taxYear
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      self.taxYear:int = obj["taxYear"]
      pass

class GetNewPRW2Dtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRW2Dtl
   whereClausePRW2DtlBox
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRW2Dtl:str = obj["whereClausePRW2Dtl"]
      self.whereClausePRW2DtlBox:str = obj["whereClausePRW2DtlBox"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRW2DtlTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class LeaveTaxYear_input:
   """ Required : 
   TaxYrFill
   """  
   def __init__(self, obj):
      self.TaxYrFill:int = obj["TaxYrFill"]
      """  Tax Year  """  
      pass

class LeaveTaxYear_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPRW2DtlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPRW2DtlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRW2DtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateUser_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass


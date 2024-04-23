import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustCntSvc
# Description: Customer Contact Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustCnts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCnts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts",headers=creds) as resp:
           return await resp.json()

async def post_CustCnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustCnts_Company_CustNum_ShipToNum_ConNum(Company, CustNum, ShipToNum, ConNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCnt item
   Description: Calls GetByID to retrieve the CustCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustCnts_Company_CustNum_ShipToNum_ConNum(Company, CustNum, ShipToNum, ConNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustCnt for the service
   Description: Calls UpdateExt to update CustCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustCnts_Company_CustNum_ShipToNum_ConNum(Company, CustNum, ShipToNum, ConNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustCnt item
   Description: Call UpdateExt to delete CustCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCnts_Company_CustNum_ShipToNum_ConNum_CustCntAttches(Company, CustNum, ShipToNum, ConNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CustCntAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustCntAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches",headers=creds) as resp:
           return await resp.json()

async def get_CustCnts_Company_CustNum_ShipToNum_ConNum_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCntAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustCntAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCntAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches",headers=creds) as resp:
           return await resp.json()

async def post_CustCntAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCntAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustCntAttch for the service
   Description: Calls UpdateExt to update CustCntAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustCntAttch item
   Description: Call UpdateExt to delete CustCntAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCustCnt, whereClauseCustCntAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCustCnt=" + whereClauseCustCnt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustCntAttch=" + whereClauseCustCntAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, shipToNum, conNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
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
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "conNum=" + conNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCustCntGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustCntGlobalFields
   OperationID: GetCustCntGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustCntGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckEFFieldLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEFFieldLength
   Description: This method checks the Customer Name and address fields to see if they conform
to the length allowed in an External Financials integration.  Will return a list of fields
longer than allowed to allow the users to change them or accept that they will be
truncated when sent to External Financials.  Needs to be run right before update.  If the user
answers no to the question then the update method should not be run.
   OperationID: CheckEFFieldLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEFFieldLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEFFieldLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultName
   Description: This method populates the detail fields from CustCnt.Name when targetName = "Detail".
When targetField = "Name", then the CustCnt.Name is built from the detail fields.
   OperationID: DefaultName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbCustCntList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbCustCntList
   Description: This method returns the GlbCustCnt dataset like GetList() method
GlbCustCnt.CustNum gt 0 indicates linked GlbCustCnt records
GlbCustCnt.CustNum lt = 0 indicates unlinked GlbCustCnt records
   OperationID: GetGlbCustCntList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbCustCntList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCustCntList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshGlbCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshGlbCustCnt
   Description: Refresh GlbCustCnt record after linking
   OperationID: RefreshGlbCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbCustCnt
   Description: Mark unlinked GlbCustCnt records as skipped
   OperationID: SkipGlbCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipSingleGlbCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipSingleGlbCustCnt
   Description: Mark a specified GlbCustCnt record as skipped
   OperationID: SkipSingleGlbCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustCntForShipTos(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustCntForShipTos
   Description: This method returns the CustCnt table populated for specific CustNum and list of ShipToNum
   OperationID: GetCustCntForShipTos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustCntForShipTos_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntForShipTos_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbCustCntRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbCustCntRef
   Description: Invokes LinkGlbCustCnt but returns CustCntTableset as ref
   OperationID: LinkGlbCustCntRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCustCntRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCustCntRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbCustCnt
   Description: This method performs the actual logic behind linking a contact.  It is run after
the PreLinkGlbCustCnt method which determines the Contact to link to.
If the Contact Number is for a Contact that already exists, the GlbCustCnt information is
translated and then copied to the CustCntDataSet as an update.
If the Contact Number is for a new Contact, the GlbCustCnt information is translated and then
copied to the CustCntDataSet as an Add.  Until the update method is run on CustCnt record
the Link process is not completed.
   OperationID: LinkGlbCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAltShipToContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAltShipToContact
   Description: This sets the ShipTo table based on the MasterCustNum and MasterShipToNum fields.
To be used when the alternate fields change
   OperationID: OnChangeAltShipToContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAltShipToContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAltShipToContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustCntPerConAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustCntPerConAddress
   Description: This method updates the address fields based on the PerConAddress being changed
   OperationID: OnChangeCustCntPerConAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustCntPerConAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustCntPerConAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpecialAddressChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpecialAddressChange
   Description: This method clears or sets the Address fields based on the SpecialAddress flag.
If CustCnt.SpecialAddress is checked then the address fields are defaulted from the Customer.
   OperationID: SpecialAddressChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpecialAddressChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpecialAddressChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustCntAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustCntAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCntAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustCntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustCntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustCntAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustCntListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustCntRow] = obj["value"]
      pass

class Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      """  The full name of the customer.  """  
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the customer contact  is synchronized to an External CRM.  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  This field holds the id of this customer in the External CRM  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  This field holds the id of this customer contact in the External CRM  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      """   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  """  
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      """   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  """  
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      """   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckEFFieldLength_input:
   """ Required : 
   vCustNum
   vShipToNum
   vConNum
   vName
   vAddress1
   vAddress2
   vAddress3
   vCity
   vState
   vCorpName
   vFirstName
   vMiddleName
   vLastName
   vInitials
   """  
   def __init__(self, obj):
      self.vCustNum:int = obj["vCustNum"]
      """  CustCnt.CustNum  """  
      self.vShipToNum:str = obj["vShipToNum"]
      """  CustCnt.ShipToNum  """  
      self.vConNum:int = obj["vConNum"]
      """  CustCnt.ConNum  """  
      self.vName:str = obj["vName"]
      """  CustCnt.Name  """  
      self.vAddress1:str = obj["vAddress1"]
      """  CustCnt.Address1  """  
      self.vAddress2:str = obj["vAddress2"]
      """  CustCnt.Address2  """  
      self.vAddress3:str = obj["vAddress3"]
      """  CustCnt.Address3  """  
      self.vCity:str = obj["vCity"]
      """  CustCnt.City  """  
      self.vState:str = obj["vState"]
      """  CustCnt.State  """  
      self.vCorpName:str = obj["vCorpName"]
      """  CustCnt.CorpName  """  
      self.vFirstName:str = obj["vFirstName"]
      """  CustCnt.FirstName  """  
      self.vMiddleName:str = obj["vMiddleName"]
      """  CustCnt.MiddleName  """  
      self.vLastName:str = obj["vLastName"]
      """  CustCnt.LastName  """  
      self.vInitials:str = obj["vInitials"]
      """  CustCnt.Initials  """  
      pass

class CheckEFFieldLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultName_input:
   """ Required : 
   targetField
   custNum
   shipToNum
   conNum
   ds
   """  
   def __init__(self, obj):
      self.targetField:str = obj["targetField"]
      """  Indicates which fields to populate either "Detail" or "Name"  """  
      self.custNum:int = obj["custNum"]
      """  CustCnt.CustNum  """  
      self.shipToNum:str = obj["shipToNum"]
      """  CustCnt.ShipToNum  """  
      self.conNum:int = obj["conNum"]
      """  CustCnt.ConNum  """  
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class DefaultName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.conNum:int = obj["conNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      """  The full name of the customer.  """  
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntListTableset:
   def __init__(self, obj):
      self.CustCntList:list[Erp_Tablesets_CustCntListRow] = obj["CustCntList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the customer contact  is synchronized to an External CRM.  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  This field holds the id of this customer in the External CRM  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  This field holds the id of this customer contact in the External CRM  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      """   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  """  
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      """   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  """  
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      """   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntTableset:
   def __init__(self, obj):
      self.CustCnt:list[Erp_Tablesets_CustCntRow] = obj["CustCnt"]
      self.CustCntAttch:list[Erp_Tablesets_CustCntAttchRow] = obj["CustCntAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCustCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Name of contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Contacts mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  see Address1.  """  
      self.Address3:str = obj["Address3"]
      """  See Address 1  """  
      self.City:str = obj["City"]
      """  see address1  """  
      self.State:str = obj["State"]
      """  Special State ID. ( See Address1 )  Can be blank.  """  
      self.Zip:str = obj["Zip"]
      """  Special Zip (see Address1 )  """  
      self.Country:str = obj["Country"]
      """  Special Country is used as part of the mailing address. It can be left blank. ( See Address1 )  """  
      self.CorpName:str = obj["CorpName"]
      """  Contacts mailing address company name if different than that of the customer.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of contact person.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is not included in marketing lists  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbShipToNum:str = obj["GlbShipToNum"]
      """  Global ShipToNumber.  This is the number in the parent company  """  
      self.GlbConNum:int = obj["GlbConNum"]
      """  This is the Contact Number of the parent company  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldCustNum:int = obj["OldCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.OldShipToNum:str = obj["OldShipToNum"]
      """  Original ShipToNumber.  This is the number in the original owner's parent company - NOT CURRENTLY IN USE  """  
      self.OldConNum:int = obj["OldConNum"]
      """  This is the Contact Number of the original parent company - CURRENTLY NOT IN USE  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global customer contacts.  The user can come back at a later time and choose to link a skipped customer contact if they need to.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.MasterConNum:int = obj["MasterConNum"]
      self.MasterCustNum:int = obj["MasterCustNum"]
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      self.FaceBook:str = obj["FaceBook"]
      self.IM:str = obj["IM"]
      self.LinkedIn:str = obj["LinkedIn"]
      self.PerConID:int = obj["PerConID"]
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      self.Twitter:str = obj["Twitter"]
      self.WebLink1:str = obj["WebLink1"]
      self.WebLink2:str = obj["WebLink2"]
      self.WebLink3:str = obj["WebLink3"]
      self.WebLink4:str = obj["WebLink4"]
      self.WebLink5:str = obj["WebLink5"]
      self.WebSite:str = obj["WebSite"]
      self.PerConAddress:bool = obj["PerConAddress"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  SyncToExternalCRM  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  ExternalCRMCustomerID  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  ExternalCRMContactID  """  
      self.LinkConNum:int = obj["LinkConNum"]
      """  Local Contact Number to Link to  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.IsLinked:bool = obj["IsLinked"]
      """  Indicates if the record is linked  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCustCntTableset:
   def __init__(self, obj):
      self.GlbCustCnt:list[Erp_Tablesets_GlbCustCntRow] = obj["GlbCustCnt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCustCntTableset:
   def __init__(self, obj):
      self.CustCnt:list[Erp_Tablesets_CustCntRow] = obj["CustCnt"]
      self.CustCntAttch:list[Erp_Tablesets_CustCntAttchRow] = obj["CustCntAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.conNum:int = obj["conNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
      pass

class GetCustCntForShipTos_input:
   """ Required : 
   company
   custNum
   shipToNumList
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company to return records for  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number to return records for  """  
      self.shipToNumList:str = obj["shipToNumList"]
      """  List of ShipToNum's to return records for  """  
      pass

class GetCustCntForShipTos_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
      pass

class GetCustCntGlobalFields_input:
   """ Required : 
   CustNum
   ShiptoNum
   ConNum
   """  
   def __init__(self, obj):
      self.CustNum:int = obj["CustNum"]
      self.ShiptoNum:str = obj["ShiptoNum"]
      self.ConNum:int = obj["ConNum"]
      pass

class GetCustCntGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGlbCustCntList_input:
   """ Required : 
   inCompany
   inGlbCompany
   inGlbCustNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.inCompany:str = obj["inCompany"]
      """  Company to return records for  """  
      self.inGlbCompany:str = obj["inGlbCompany"]
      """  Global Company to return records for  """  
      self.inGlbCustNum:int = obj["inGlbCustNum"]
      """  Global Customer to return records for  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetGlbCustCntList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCustCntTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_CustCntListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustCntAttch_input:
   """ Required : 
   ds
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.conNum:int = obj["conNum"]
      pass

class GetNewCustCntAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCustCnt_input:
   """ Required : 
   ds
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetNewCustCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   PerConID
   ds
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCustCnt
   whereClauseCustCntAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCustCnt:str = obj["whereClauseCustCnt"]
      self.whereClauseCustCntAttch:str = obj["whereClauseCustCntAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
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

class LinkGlbCustCntRef_input:
   """ Required : 
   glbCompany
   glbCustNum
   glbShipToNum
   glbConNum
   ds
   dsCustCnt
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbCustNum:int = obj["glbCustNum"]
      self.glbShipToNum:str = obj["glbShipToNum"]
      self.glbConNum:int = obj["glbConNum"]
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      self.dsCustCnt:list[Erp_Tablesets_CustCntTableset] = obj["dsCustCnt"]
      pass

class LinkGlbCustCntRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsCustCnt:list[Erp_Tablesets_CustCntTableset] = obj["dsCustCnt"]
      pass

      """  output parameters  """  

class LinkGlbCustCnt_input:
   """ Required : 
   glbCompany
   glbCustNum
   glbShipToNum
   glbConNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCustCnt record to link  """  
      self.glbCustNum:int = obj["glbCustNum"]
      """  Global CustNum field on the GlbCustCnt record to link  """  
      self.glbShipToNum:str = obj["glbShipToNum"]
      """  Global ShipToNum field on the GlbCustCnt record to link  """  
      self.glbConNum:int = obj["glbConNum"]
      """  Global ConNum field on the GlbCustCnt record to link  """  
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

class LinkGlbCustCnt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAltShipToContact_input:
   """ Required : 
   iProposedMasterCustID
   iProposedMasterShipToNum
   iProposedMasterConNum
   ds
   """  
   def __init__(self, obj):
      self.iProposedMasterCustID:str = obj["iProposedMasterCustID"]
      """  The proposed CustID value  """  
      self.iProposedMasterShipToNum:str = obj["iProposedMasterShipToNum"]
      """  The proposed ShipTo Num value  """  
      self.iProposedMasterConNum:int = obj["iProposedMasterConNum"]
      """  The proposed Contact number value  """  
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class OnChangeAltShipToContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCustCntPerConAddress_input:
   """ Required : 
   conNum
   proposedPerConAddress
   ds
   """  
   def __init__(self, obj):
      self.conNum:int = obj["conNum"]
      self.proposedPerConAddress:bool = obj["proposedPerConAddress"]
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class OnChangeCustCntPerConAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshGlbCustCnt_input:
   """ Required : 
   glbCompany
   glbCustNum
   glbShipToNum
   glbConNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbCustNum:int = obj["glbCustNum"]
      """  Global Customer Number  """  
      self.glbShipToNum:str = obj["glbShipToNum"]
      """  Global Ship To Number  """  
      self.glbConNum:int = obj["glbConNum"]
      """  Global Contact Number  """  
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

class RefreshGlbCustCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipGlbCustCnt_input:
   """ Required : 
   glbCompany
   glbCustNum
   glbShipToNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbCustNum:int = obj["glbCustNum"]
      """  Global Customer Number  """  
      self.glbShipToNum:str = obj["glbShipToNum"]
      """  Global Ship To Number  """  
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

class SkipGlbCustCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipSingleGlbCustCnt_input:
   """ Required : 
   glbCompany
   glbCustNum
   glbShipToNum
   glbConNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbCustNum:int = obj["glbCustNum"]
      """  Global Customer Number  """  
      self.glbShipToNum:str = obj["glbShipToNum"]
      """  Global Ship To Number  """  
      self.glbConNum:int = obj["glbConNum"]
      """  Global Contact Number  """  
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

class SkipSingleGlbCustCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SpecialAddressChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class SpecialAddressChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustCntTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustCntTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustCntTableset] = obj["ds"]
      pass

      """  output parameters  """  


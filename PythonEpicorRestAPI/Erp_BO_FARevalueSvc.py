import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FARevalueSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FARevalues(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FARevalues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalues
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues",headers=creds) as resp:
           return await resp.json()

async def post_FARevalues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FARevalues_Company_AssetNum_RevalueNum(Company, AssetNum, RevalueNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalue item
   Description: Calls GetByID to retrieve the FARevalue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FARevalues_Company_AssetNum_RevalueNum(Company, AssetNum, RevalueNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FARevalue for the service
   Description: Calls UpdateExt to update FARevalue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FARevalues_Company_AssetNum_RevalueNum(Company, AssetNum, RevalueNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FARevalue item
   Description: Call UpdateExt to delete FARevalue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FARevalues_Company_AssetNum_RevalueNum_FARevalueRegs(Company, AssetNum, RevalueNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FARevalueRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FARevalueRegs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueRegs",headers=creds) as resp:
           return await resp.json()

async def get_FARevalues_Company_AssetNum_RevalueNum_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalueReg item
   Description: Calls GetByID to retrieve the FARevalueReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueReg1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FARevalues_Company_AssetNum_RevalueNum_FARevalueAttches(Company, AssetNum, RevalueNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FARevalueAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FARevalueAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueAttches",headers=creds) as resp:
           return await resp.json()

async def get_FARevalues_Company_AssetNum_RevalueNum_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company, AssetNum, RevalueNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalueAttch item
   Description: Calls GetByID to retrieve the FARevalueAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalues(" + Company + "," + AssetNum + "," + RevalueNum + ")/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FARevalueRegs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FARevalueRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueRegs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs",headers=creds) as resp:
           return await resp.json()

async def post_FARevalueRegs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalueReg item
   Description: Calls GetByID to retrieve the FARevalueReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FARevalueReg for the service
   Description: Calls UpdateExt to update FARevalueReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FARevalueRegs_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FARevalueReg item
   Description: Call UpdateExt to delete FARevalueReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueRegs(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FARevalueAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FARevalueAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches",headers=creds) as resp:
           return await resp.json()

async def post_FARevalueAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company, AssetNum, RevalueNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalueAttch item
   Description: Calls GetByID to retrieve the FARevalueAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company, AssetNum, RevalueNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FARevalueAttch for the service
   Description: Calls UpdateExt to update FARevalueAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FARevalueAttches_Company_AssetNum_RevalueNum_DrawingSeq(Company, AssetNum, RevalueNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FARevalueAttch item
   Description: Call UpdateExt to delete FARevalueAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/FARevalueAttches(" + Company + "," + AssetNum + "," + RevalueNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFARevalue, whereClauseFARevalueAttch, whereClauseFARevalueReg, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFARevalue=" + whereClauseFARevalue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFARevalueAttch=" + whereClauseFARevalueAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFARevalueReg=" + whereClauseFARevalueReg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, revalueNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revalueNum=" + revalueNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRevaluation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRevaluation
   Description: Get New Revaluation (Substitute method for FARevalueGetNew)
It is required to put ValuationDate and ApplyDate here.
Standart FARevalueGetNew is generated with AssetNum input parameter only
   OperationID: GetNewRevaluation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRevaluation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRevaluation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevaluationsWithRecalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevaluationsWithRecalc
   Description: Return asset's revaluations with registers recalculated
   OperationID: GetRevaluationsWithRecalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevaluationsWithRecalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevaluationsWithRecalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableApplyDate
   OperationID: GetAvailableApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultDates
   OperationID: GetDefaultDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckApplyDateInClosedPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckApplyDateInClosedPer
   OperationID: CheckApplyDateInClosedPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckApplyDateInClosedPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckApplyDateInClosedPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetDepRecalcNeeded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetDepRecalcNeeded
   Description: Check if the asset or any of its registers requires depreciation calculation
   OperationID: CheckAssetDepRecalcNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetDepRecalcNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetDepRecalcNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNewBookValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNewBookValue
   Description: Calculates the New Book Values amounts for Revaluation.
   OperationID: OnChangeNewBookValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNewBookValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNewBookValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNewResidualValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNewResidualValue
   Description: Calculates the New Residual Values amounts for Revaluation Register Details.
   OperationID: OnChangeNewResidualValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNewResidualValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNewResidualValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReadyToPost
   OperationID: OnChangeReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeApplyDate
   OperationID: OnChangeApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeValuationDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeValuationDate
   OperationID: OnChangeValuationDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeValuationDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeValuationDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRegistersInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRegistersInfo
   OperationID: GetNewRegistersInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRegistersInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRegistersInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseDateValidationMessage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseDateValidationMessage
   Description: Parse warning Msg from date validation method.
   OperationID: ParseDateValidationMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseDateValidationMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseDateValidationMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFARevalue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFARevalue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFARevalueAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFARevalueAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFARevalueReg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFARevalueReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueRegRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueRow] = obj["value"]
      pass

class Erp_Tablesets_FARevalueAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.RevalueNum:int = obj["RevalueNum"]
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

class Erp_Tablesets_FARevalueListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.OrigCurrentCost:int = obj["OrigCurrentCost"]
      """  The original Current Asset Cost in base currency before running the Asset Revaluation process.  """  
      self.DocOrigCurrentCost:int = obj["DocOrigCurrentCost"]
      """  The original Current Asset Cost in document currency before running the Asset Revaluation process.  """  
      self.Rpt1OrigCurrentCost:int = obj["Rpt1OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt2OrigCurrentCost:int = obj["Rpt2OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt3OrigCurrentCost:int = obj["Rpt3OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.OrigBookValue:int = obj["OrigBookValue"]
      """  Book Value before revaluation in base currency.  """  
      self.DocOrigBookValue:int = obj["DocOrigBookValue"]
      """  Book Value before revaluation in document currency.  """  
      self.Rpt1OrigBookValue:int = obj["Rpt1OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt2OrigBookValue:int = obj["Rpt2OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt3OrigBookValue:int = obj["Rpt3OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.OrigTotalDepn:int = obj["OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  """  
      self.DocOrigTotalDepn:int = obj["DocOrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  """  
      self.Rpt1OrigTotalDepn:int = obj["Rpt1OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt2OrigTotalDepn:int = obj["Rpt2OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt3OrigTotalDepn:int = obj["Rpt3OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.RevalueSurplus:int = obj["RevalueSurplus"]
      """  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.DocRevalueSurplus:int = obj["DocRevalueSurplus"]
      """  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt1RevalueSurplus:int = obj["Rpt1RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt2RevalueSurplus:int = obj["Rpt2RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt3RevalueSurplus:int = obj["Rpt3RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.GrantDepnAmt:int = obj["GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantDepnAmt:int = obj["DocGrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantDepnAmt:int = obj["Rpt1GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantDepnAmt:int = obj["Rpt2GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantDepnAmt:int = obj["Rpt3GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.UnusedGrantAmt:int = obj["UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in base currency.  """  
      self.DocUnusedGrantAmt:int = obj["DocUnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in document currency.  """  
      self.Rpt1UnusedGrantAmt:int = obj["Rpt1UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt2UnusedGrantAmt:int = obj["Rpt2UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt3UnusedGrantAmt:int = obj["Rpt3UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.PostedFutrDepnAmt:int = obj["PostedFutrDepnAmt"]
      """  The Depreciation value in the base currency posted to the GL after Revaluation Date.  """  
      self.DocPostedFutrDepnAmt:int = obj["DocPostedFutrDepnAmt"]
      """  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  """  
      self.Rpt1PostedFutrDepnAmt:int = obj["Rpt1PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrDepnAmt:int = obj["Rpt2PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrDepnAmt:int = obj["Rpt3PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.PostedFutrGrantDepnAmt:int = obj["PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  """  
      self.DocPostedFutrGrantDepnAmt:int = obj["DocPostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  """  
      self.Rpt1PostedFutrGrantDepnAmt:int = obj["Rpt1PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrGrantDepnAmt:int = obj["Rpt2PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrGrantDepnAmt:int = obj["Rpt3PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.NewResidualValue:int = obj["NewResidualValue"]
      """  New Residual value of the asset in base currency. By default it is equaled current value.  """  
      self.DocNewResidualValue:int = obj["DocNewResidualValue"]
      """  New Residual value of the asset in document currency. By default it is equaled current value.  """  
      self.Rpt1NewResidualValue:int = obj["Rpt1NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt2NewResidualValue:int = obj["Rpt2NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt3NewResidualValue:int = obj["Rpt3NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision Identifier for this row. It is incremented upon oach write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  """  
      self.OrigCurrPerDepn:int = obj["OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerDepn:int = obj["DocOrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerDepn:int = obj["Rpt1OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerDepn:int = obj["Rpt2OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerDepn:int = obj["Rpt3OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.OrigCurrPerGrantDepn:int = obj["OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerGrantDepn:int = obj["DocOrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerGrantDepn:int = obj["Rpt1OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerGrantDepn:int = obj["Rpt2OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerGrantDepn:int = obj["Rpt3OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.AssetRegDescription:str = obj["AssetRegDescription"]
      self.CurrAssetLife:int = obj["CurrAssetLife"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrLifeModifier:str = obj["CurrLifeModifier"]
      self.DocResidualValue:int = obj["DocResidualValue"]
      self.ResidualValue:int = obj["ResidualValue"]
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetDtlRpt1ResidualValue:int = obj["FAssetDtlRpt1ResidualValue"]
      self.FAssetDtlDocResidualValue:int = obj["FAssetDtlDocResidualValue"]
      self.FAssetDtlRpt2ResidualValue:int = obj["FAssetDtlRpt2ResidualValue"]
      self.FAssetDtlRpt3ResidualValue:int = obj["FAssetDtlRpt3ResidualValue"]
      self.FAssetDtlLifeModifier:str = obj["FAssetDtlLifeModifier"]
      self.FAssetDtlAssetLife:int = obj["FAssetDtlAssetLife"]
      self.FAssetDtlResidualValue:int = obj["FAssetDtlResidualValue"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Revaluation.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.NewBookValue:int = obj["NewBookValue"]
      """  New Book Value in base currency.  """  
      self.DocNewBookValue:int = obj["DocNewBookValue"]
      """  New Book Value in document currency.  """  
      self.Rpt1NewBookValue:int = obj["Rpt1NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.Rpt2NewBookValue:int = obj["Rpt2NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.Rpt3NewBookValue:int = obj["Rpt3NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.RevalueMethod:str = obj["RevalueMethod"]
      """   Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.CostLimitApplied:bool = obj["CostLimitApplied"]
      """  Flag to indicate if Cost Limit is applied.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ValuationDate:str = obj["ValuationDate"]
      """  Valuation Date is an invormation field , but it is default for the Apply date.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckApplyDateInClosedPer_input:
   """ Required : 
   assetNum
   applyDate
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.applyDate:str = obj["applyDate"]
      pass

class CheckApplyDateInClosedPer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckAssetDepRecalcNeeded_input:
   """ Required : 
   assetNum
   applyDate
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.applyDate:str = obj["applyDate"]
      """  Revaluation Apply Date  """  
      pass

class CheckAssetDepRecalcNeeded_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  true if depreciation calculation is required  """  
      pass

class CheckAssetTransactions_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class CheckAssetTransactions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: null  """  
      pass

class ClearReadyToPost_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class ClearReadyToPost_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   assetNum
   revalueNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FARevalueAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.RevalueNum:int = obj["RevalueNum"]
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

class Erp_Tablesets_FARevalueListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueListTableset:
   def __init__(self, obj):
      self.FARevalueList:list[Erp_Tablesets_FARevalueListRow] = obj["FARevalueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FARevalueRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.OrigCurrentCost:int = obj["OrigCurrentCost"]
      """  The original Current Asset Cost in base currency before running the Asset Revaluation process.  """  
      self.DocOrigCurrentCost:int = obj["DocOrigCurrentCost"]
      """  The original Current Asset Cost in document currency before running the Asset Revaluation process.  """  
      self.Rpt1OrigCurrentCost:int = obj["Rpt1OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt2OrigCurrentCost:int = obj["Rpt2OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt3OrigCurrentCost:int = obj["Rpt3OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.OrigBookValue:int = obj["OrigBookValue"]
      """  Book Value before revaluation in base currency.  """  
      self.DocOrigBookValue:int = obj["DocOrigBookValue"]
      """  Book Value before revaluation in document currency.  """  
      self.Rpt1OrigBookValue:int = obj["Rpt1OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt2OrigBookValue:int = obj["Rpt2OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt3OrigBookValue:int = obj["Rpt3OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.OrigTotalDepn:int = obj["OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  """  
      self.DocOrigTotalDepn:int = obj["DocOrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  """  
      self.Rpt1OrigTotalDepn:int = obj["Rpt1OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt2OrigTotalDepn:int = obj["Rpt2OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt3OrigTotalDepn:int = obj["Rpt3OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.RevalueSurplus:int = obj["RevalueSurplus"]
      """  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.DocRevalueSurplus:int = obj["DocRevalueSurplus"]
      """  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt1RevalueSurplus:int = obj["Rpt1RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt2RevalueSurplus:int = obj["Rpt2RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt3RevalueSurplus:int = obj["Rpt3RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.GrantDepnAmt:int = obj["GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantDepnAmt:int = obj["DocGrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantDepnAmt:int = obj["Rpt1GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantDepnAmt:int = obj["Rpt2GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantDepnAmt:int = obj["Rpt3GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.UnusedGrantAmt:int = obj["UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in base currency.  """  
      self.DocUnusedGrantAmt:int = obj["DocUnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in document currency.  """  
      self.Rpt1UnusedGrantAmt:int = obj["Rpt1UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt2UnusedGrantAmt:int = obj["Rpt2UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt3UnusedGrantAmt:int = obj["Rpt3UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.PostedFutrDepnAmt:int = obj["PostedFutrDepnAmt"]
      """  The Depreciation value in the base currency posted to the GL after Revaluation Date.  """  
      self.DocPostedFutrDepnAmt:int = obj["DocPostedFutrDepnAmt"]
      """  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  """  
      self.Rpt1PostedFutrDepnAmt:int = obj["Rpt1PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrDepnAmt:int = obj["Rpt2PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrDepnAmt:int = obj["Rpt3PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.PostedFutrGrantDepnAmt:int = obj["PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  """  
      self.DocPostedFutrGrantDepnAmt:int = obj["DocPostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  """  
      self.Rpt1PostedFutrGrantDepnAmt:int = obj["Rpt1PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrGrantDepnAmt:int = obj["Rpt2PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrGrantDepnAmt:int = obj["Rpt3PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.NewResidualValue:int = obj["NewResidualValue"]
      """  New Residual value of the asset in base currency. By default it is equaled current value.  """  
      self.DocNewResidualValue:int = obj["DocNewResidualValue"]
      """  New Residual value of the asset in document currency. By default it is equaled current value.  """  
      self.Rpt1NewResidualValue:int = obj["Rpt1NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt2NewResidualValue:int = obj["Rpt2NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt3NewResidualValue:int = obj["Rpt3NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision Identifier for this row. It is incremented upon oach write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  """  
      self.OrigCurrPerDepn:int = obj["OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerDepn:int = obj["DocOrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerDepn:int = obj["Rpt1OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerDepn:int = obj["Rpt2OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerDepn:int = obj["Rpt3OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.OrigCurrPerGrantDepn:int = obj["OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerGrantDepn:int = obj["DocOrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerGrantDepn:int = obj["Rpt1OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerGrantDepn:int = obj["Rpt2OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerGrantDepn:int = obj["Rpt3OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.AssetRegDescription:str = obj["AssetRegDescription"]
      self.CurrAssetLife:int = obj["CurrAssetLife"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrLifeModifier:str = obj["CurrLifeModifier"]
      self.DocResidualValue:int = obj["DocResidualValue"]
      self.ResidualValue:int = obj["ResidualValue"]
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetDtlRpt1ResidualValue:int = obj["FAssetDtlRpt1ResidualValue"]
      self.FAssetDtlDocResidualValue:int = obj["FAssetDtlDocResidualValue"]
      self.FAssetDtlRpt2ResidualValue:int = obj["FAssetDtlRpt2ResidualValue"]
      self.FAssetDtlRpt3ResidualValue:int = obj["FAssetDtlRpt3ResidualValue"]
      self.FAssetDtlLifeModifier:str = obj["FAssetDtlLifeModifier"]
      self.FAssetDtlAssetLife:int = obj["FAssetDtlAssetLife"]
      self.FAssetDtlResidualValue:int = obj["FAssetDtlResidualValue"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Revaluation.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.NewBookValue:int = obj["NewBookValue"]
      """  New Book Value in base currency.  """  
      self.DocNewBookValue:int = obj["DocNewBookValue"]
      """  New Book Value in document currency.  """  
      self.Rpt1NewBookValue:int = obj["Rpt1NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.Rpt2NewBookValue:int = obj["Rpt2NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.Rpt3NewBookValue:int = obj["Rpt3NewBookValue"]
      """  New Book Value in reporting currency.  """  
      self.RevalueMethod:str = obj["RevalueMethod"]
      """   Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.CostLimitApplied:bool = obj["CostLimitApplied"]
      """  Flag to indicate if Cost Limit is applied.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ValuationDate:str = obj["ValuationDate"]
      """  Valuation Date is an invormation field , but it is default for the Apply date.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.IsLocked:bool = obj["IsLocked"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueTableset:
   def __init__(self, obj):
      self.FARevalue:list[Erp_Tablesets_FARevalueRow] = obj["FARevalue"]
      self.FARevalueAttch:list[Erp_Tablesets_FARevalueAttchRow] = obj["FARevalueAttch"]
      self.FARevalueReg:list[Erp_Tablesets_FARevalueRegRow] = obj["FARevalueReg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFARevalueTableset:
   def __init__(self, obj):
      self.FARevalue:list[Erp_Tablesets_FARevalueRow] = obj["FARevalue"]
      self.FARevalueAttch:list[Erp_Tablesets_FARevalueAttchRow] = obj["FARevalueAttch"]
      self.FARevalueReg:list[Erp_Tablesets_FARevalueRegRow] = obj["FARevalueReg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailableApplyDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class GetAvailableApplyDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   assetNum
   revalueNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FARevalueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueTableset] = obj["returnObj"]
      pass

class GetDefaultDates_input:
   """ Required : 
   assetNum
   valuationDate
   applyDate
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.valuationDate:str = obj["valuationDate"]
      self.applyDate:str = obj["applyDate"]
      pass

class GetDefaultDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.valuationDate:str = obj["parameters"]
      self.applyDate:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFARevalueAttch_input:
   """ Required : 
   ds
   assetNum
   revalueNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      pass

class GetNewFARevalueAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFARevalueReg_input:
   """ Required : 
   ds
   assetNum
   revalueNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      pass

class GetNewFARevalueReg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFARevalue_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFARevalue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRegistersInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class GetNewRegistersInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewRevaluation_input:
   """ Required : 
   assetNum
   valuationDate
   applyDate
   ds
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset Number  """  
      self.valuationDate:str = obj["valuationDate"]
      """  Valuation Date  """  
      self.applyDate:str = obj["applyDate"]
      """  Apply Date  """  
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class GetNewRevaluation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRevaluationsWithRecalc_input:
   """ Required : 
   assetNum
   ds
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class GetRevaluationsWithRecalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFARevalue
   whereClauseFARevalueAttch
   whereClauseFARevalueReg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFARevalue:str = obj["whereClauseFARevalue"]
      self.whereClauseFARevalueAttch:str = obj["whereClauseFARevalueAttch"]
      self.whereClauseFARevalueReg:str = obj["whereClauseFARevalueReg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FARevalueTableset] = obj["returnObj"]
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

class OnChangeApplyDate_input:
   """ Required : 
   applyDate
   ds
   """  
   def __init__(self, obj):
      self.applyDate:str = obj["applyDate"]
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class OnChangeApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeNewBookValue_input:
   """ Required : 
   newBookValue
   ds
   """  
   def __init__(self, obj):
      self.newBookValue:int = obj["newBookValue"]
      """  new Book value  """  
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class OnChangeNewBookValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeNewResidualValue_input:
   """ Required : 
   newResidualValue
   ds
   """  
   def __init__(self, obj):
      self.newResidualValue:int = obj["newResidualValue"]
      """  new Residual Value  """  
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class OnChangeNewResidualValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeReadyToPost_input:
   """ Required : 
   readyToPost
   ds
   """  
   def __init__(self, obj):
      self.readyToPost:bool = obj["readyToPost"]
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class OnChangeReadyToPost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeValuationDate_input:
   """ Required : 
   valuationDate
   ds
   """  
   def __init__(self, obj):
      self.valuationDate:str = obj["valuationDate"]
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class OnChangeValuationDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ParseDateValidationMessage_input:
   """ Required : 
   warnMsg
   """  
   def __init__(self, obj):
      self.warnMsg:str = obj["warnMsg"]
      pass

class ParseDateValidationMessage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDialogInfo1:str = obj["parameters"]
      self.opDialogInfo2:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFARevalueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFARevalueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  


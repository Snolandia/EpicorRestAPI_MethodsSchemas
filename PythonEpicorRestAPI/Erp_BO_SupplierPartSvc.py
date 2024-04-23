import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SupplierPartSvc
# Description: Supplier Part BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SupplierParts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SupplierParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts",headers=creds) as resp:
           return await resp.json()

async def post_SupplierParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SupplierParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SupplierPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SupplierPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SupplierParts_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SupplierPart item
   Description: Calls GetByID to retrieve the SupplierPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SupplierParts_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SupplierPart for the service
   Description: Calls UpdateExt to update SupplierPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SupplierPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SupplierPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SupplierParts_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SupplierPart item
   Description: Call UpdateExt to delete SupplierPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SupplierPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SupplierParts_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_SupplierPartAttches(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SupplierPartAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SupplierPartAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")/SupplierPartAttches",headers=creds) as resp:
           return await resp.json()

async def get_SupplierParts_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_SupplierPartAttches_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_DrawingSeq(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SupplierPartAttch item
   Description: Calls GetByID to retrieve the SupplierPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierPartAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierParts(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")/SupplierPartAttches(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SupplierPartAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SupplierPartAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierPartAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierPartAttches",headers=creds) as resp:
           return await resp.json()

async def post_SupplierPartAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SupplierPartAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SupplierPartAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SupplierPartAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierPartAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SupplierPartAttches_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_DrawingSeq(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SupplierPartAttch item
   Description: Calls GetByID to retrieve the SupplierPartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierPartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierPartAttches(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SupplierPartAttches_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_DrawingSeq(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SupplierPartAttch for the service
   Description: Calls UpdateExt to update SupplierPartAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SupplierPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SupplierPartAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierPartAttches(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SupplierPartAttches_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum_DrawingSeq(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SupplierPartAttch item
   Description: Call UpdateExt to delete SupplierPartAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SupplierPartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/SupplierPartAttches(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierPartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSupplierPart, whereClauseSupplierPartAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSupplierPart=" + whereClauseSupplierPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSupplierPartAttch=" + whereClauseSupplierPartAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, vendorNum, vendPartNum, mfgNum, mfgPartNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendPartNum=" + vendPartNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mfgNum=" + mfgNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mfgPartNum=" + mfgPartNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSupplierPartMfgNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSupplierPartMfgNum
   Description: When Changing SupplierPart.MfgtNum field.
   OperationID: ChangeSupplierPartMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSupplierPartMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplierPartMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSupplierPartMfgPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSupplierPartMfgPartNum
   Description: When Changing SupplierPart.MfgPartNum field.
   OperationID: ChangeSupplierPartMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSupplierPartMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplierPartMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSupplierPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSupplierPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSupplierPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSupplierPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSupplierPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSupplierPartAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSupplierPartAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSupplierPartAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSupplierPartAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSupplierPartAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierPartAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SupplierPartAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierPartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SupplierPartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SupplierPartRow] = obj["value"]
      pass

class Erp_Tablesets_SupplierPartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
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

class Erp_Tablesets_SupplierPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Code  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Related RFQ Num. This value is taken from ttVendPart.RFQNum in Supplier Price List Entry  """  
      self.RFQLine:int = obj["RFQLine"]
      """  Related RFQ Line. This value is taken from ttVendPart.RFQLine in Supplier Price List Entry  """  
      self.MfgPartLeadTime:str = obj["MfgPartLeadTime"]
      self.MfgPartLifecycleStatus:str = obj["MfgPartLifecycleStatus"]
      self.MfgPartLifecycleDescription:str = obj["MfgPartLifecycleDescription"]
      """  Lifecycle Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeSupplierPartMfgNum_input:
   """ Required : 
   iMfgNum
   ds
   """  
   def __init__(self, obj):
      self.iMfgNum:int = obj["iMfgNum"]
      """  Manufacturer Number  """  
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

class ChangeSupplierPartMfgNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSupplierPartMfgPartNum_input:
   """ Required : 
   iMfgPartNum
   ds
   """  
   def __init__(self, obj):
      self.iMfgPartNum:str = obj["iMfgPartNum"]
      """  Manufacturer Part Number  """  
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

class ChangeSupplierPartMfgPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   partNum
   vendorNum
   vendPartNum
   mfgNum
   mfgPartNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.vendorNum:int = obj["vendorNum"]
      self.vendPartNum:str = obj["vendPartNum"]
      self.mfgNum:int = obj["mfgNum"]
      self.mfgPartNum:str = obj["mfgPartNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SupplierPartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
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

class Erp_Tablesets_SupplierPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierPartListTableset:
   def __init__(self, obj):
      self.SupplierPartList:list[Erp_Tablesets_SupplierPartListRow] = obj["SupplierPartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SupplierPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Code  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Related RFQ Num. This value is taken from ttVendPart.RFQNum in Supplier Price List Entry  """  
      self.RFQLine:int = obj["RFQLine"]
      """  Related RFQ Line. This value is taken from ttVendPart.RFQLine in Supplier Price List Entry  """  
      self.MfgPartLeadTime:str = obj["MfgPartLeadTime"]
      self.MfgPartLifecycleStatus:str = obj["MfgPartLifecycleStatus"]
      self.MfgPartLifecycleDescription:str = obj["MfgPartLifecycleDescription"]
      """  Lifecycle Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierPartTableset:
   def __init__(self, obj):
      self.SupplierPart:list[Erp_Tablesets_SupplierPartRow] = obj["SupplierPart"]
      self.SupplierPartAttch:list[Erp_Tablesets_SupplierPartAttchRow] = obj["SupplierPartAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSupplierPartTableset:
   def __init__(self, obj):
      self.SupplierPart:list[Erp_Tablesets_SupplierPartRow] = obj["SupplierPart"]
      self.SupplierPartAttch:list[Erp_Tablesets_SupplierPartAttchRow] = obj["SupplierPartAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   vendorNum
   vendPartNum
   mfgNum
   mfgPartNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.vendorNum:int = obj["vendorNum"]
      self.vendPartNum:str = obj["vendPartNum"]
      self.mfgNum:int = obj["mfgNum"]
      self.mfgPartNum:str = obj["mfgPartNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupplierPartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SupplierPartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SupplierPartTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_SupplierPartListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSupplierPartAttch_input:
   """ Required : 
   ds
   partNum
   vendorNum
   vendPartNum
   mfgNum
   mfgPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.vendorNum:int = obj["vendorNum"]
      self.vendPartNum:str = obj["vendPartNum"]
      self.mfgNum:int = obj["mfgNum"]
      self.mfgPartNum:str = obj["mfgPartNum"]
      pass

class GetNewSupplierPartAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSupplierPart_input:
   """ Required : 
   ds
   partNum
   vendorNum
   vendPartNum
   mfgNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.vendorNum:int = obj["vendorNum"]
      self.vendPartNum:str = obj["vendPartNum"]
      self.mfgNum:int = obj["mfgNum"]
      pass

class GetNewSupplierPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSupplierPart
   whereClauseSupplierPartAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSupplierPart:str = obj["whereClauseSupplierPart"]
      self.whereClauseSupplierPartAttch:str = obj["whereClauseSupplierPartAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupplierPartTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSupplierPartTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSupplierPartTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SupplierPartTableset] = obj["ds"]
      pass

      """  output parameters  """  


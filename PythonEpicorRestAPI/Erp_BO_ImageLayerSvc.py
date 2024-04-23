import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ImageLayerSvc
# Description: ImageLayerSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ImageLayers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImageLayers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImageLayers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers",headers=creds) as resp:
           return await resp.json()

async def post_ImageLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImageLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImageLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImageLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImageLayers_Company_ImageLayerID(Company, ImageLayerID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImageLayer item
   Description: Calls GetByID to retrieve the ImageLayer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImageLayer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImageLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers(" + Company + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImageLayers_Company_ImageLayerID(Company, ImageLayerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImageLayer for the service
   Description: Calls UpdateExt to update ImageLayer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImageLayer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImageLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers(" + Company + "," + ImageLayerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImageLayers_Company_ImageLayerID(Company, ImageLayerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImageLayer item
   Description: Call UpdateExt to delete ImageLayer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImageLayer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers(" + Company + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImageLayers_Company_ImageLayerID_ImageLayerDetails(Company, ImageLayerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImageLayerDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImageLayerDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers(" + Company + "," + ImageLayerID + ")/ImageLayerDetails",headers=creds) as resp:
           return await resp.json()

async def get_ImageLayers_Company_ImageLayerID_ImageLayerDetails_Company_ImageLayerID_LayerSeq(Company, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImageLayerDetail item
   Description: Calls GetByID to retrieve the ImageLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImageLayerDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImageLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayers(" + Company + "," + ImageLayerID + ")/ImageLayerDetails(" + Company + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImageLayerDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImageLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImageLayerDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayerDetails",headers=creds) as resp:
           return await resp.json()

async def post_ImageLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImageLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImageLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImageLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImageLayerDetails_Company_ImageLayerID_LayerSeq(Company, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImageLayerDetail item
   Description: Calls GetByID to retrieve the ImageLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImageLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImageLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayerDetails(" + Company + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImageLayerDetails_Company_ImageLayerID_LayerSeq(Company, ImageLayerID, LayerSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImageLayerDetail for the service
   Description: Calls UpdateExt to update ImageLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImageLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImageLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayerDetails(" + Company + "," + ImageLayerID + "," + LayerSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImageLayerDetails_Company_ImageLayerID_LayerSeq(Company, ImageLayerID, LayerSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImageLayerDetail item
   Description: Call UpdateExt to delete ImageLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImageLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/ImageLayerDetails(" + Company + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImageLayerHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseImageLayerHeader, whereClauseImageLayerDetail, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseImageLayerHeader=" + whereClauseImageLayerHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImageLayerDetail=" + whereClauseImageLayerDetail
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(imageLayerID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "imageLayerID=" + imageLayerID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateImageLayerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateImageLayerID
   Description: Duplicate specified Image Layer ID.
   OperationID: DuplicateImageLayerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateImageLayerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateImageLayerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportImageLayer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportImageLayer
   Description: Exports an Image Layer.
   OperationID: ExportImageLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportImageLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportImageLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportImageLayer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportImageLayer
   Description: Imports an Image Layer.
   OperationID: ImportImageLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportImageLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportImageLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImageLayerScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImageLayerScriptCode
   Description: Method used to call the Image Layer Engine code generator and return Script code for execution.
<param name="imageLayerID">Image Layer ID to be used for generating the script code</param>
   OperationID: ImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImageLayerUpdateScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImageLayerUpdateScriptCode
   Description: Method used to call the Image Layer Engine code generator and return Script code for execution.
<param name="imageLayerID">Image Layer ID to be used for generating the script code</param>
   OperationID: ImageLayerUpdateScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImageLayerUpdateScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImageLayerUpdateScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustomHeadersWithDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustomHeadersWithDetail
   Description: This overload of GetList returns a list of Image Layer Header records with details.
   OperationID: GetListCustomHeadersWithDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustomHeadersWithDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustomHeadersWithDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImageLayerHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImageLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImageLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImageLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImageLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImageLayerDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImageLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImageLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImageLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImageLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImageLayerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImageLayerDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImageLayerDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImageLayerHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImageLayerHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImageLayerHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImageLayerHeaderRow] = obj["value"]
      pass

class Erp_Tablesets_ImageLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  Next number within the Image Layer Header. This is assigned programattically.  """  
      self.LayerName:str = obj["LayerName"]
      """  Layer name  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  Description of layer: example hull, step, tower  """  
      self.ZIndex:int = obj["ZIndex"]
      """  ZIndex  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png types are supported  """  
      self.Category:str = obj["Category"]
      """  Free form text  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageLayerHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.ImageID:str = obj["ImageID"]
      """  Name of image the individual layers are placed upon.  """  
      self.ImageURL:str = obj["ImageURL"]
      """  ImageURL  """  
      self.Description:str = obj["Description"]
      """  Free form description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.ImageID:str = obj["ImageID"]
      """  Name of image the individual layers are placed upon.  """  
      self.ImageURL:str = obj["ImageURL"]
      """  ImageURL  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.Description:str = obj["Description"]
      """  Free form description  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Approved:bool = obj["Approved"]
      """  When true, the definition can be assigned to a PcInput.  When flase, it cannot be assigned to a PcInput.  """  
      self.Version:int = obj["Version"]
      """  Internal number updated each time the definition is approved. This is used by Verify Configuration.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  ID of the person who approved the definition for use.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the definition was approved.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateImageLayerID_input:
   """ Required : 
   company
   imageLayerID
   newImageLayerID
   newImageLayerDesc
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company of current ImageLayerID.  """  
      self.imageLayerID:str = obj["imageLayerID"]
      """  ImageLayerID we are duplicating.  """  
      self.newImageLayerID:str = obj["newImageLayerID"]
      """  New ImageLayerID name we are creating.  """  
      self.newImageLayerDesc:str = obj["newImageLayerDesc"]
      """  New Description for our new ImageLayerID.  """  
      pass

class DuplicateImageLayerID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageLayerTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_ImageLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  Next number within the Image Layer Header. This is assigned programattically.  """  
      self.LayerName:str = obj["LayerName"]
      """  Layer name  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  Description of layer: example hull, step, tower  """  
      self.ZIndex:int = obj["ZIndex"]
      """  ZIndex  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png types are supported  """  
      self.Category:str = obj["Category"]
      """  Free form text  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageLayerHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.ImageID:str = obj["ImageID"]
      """  Name of image the individual layers are placed upon.  """  
      self.ImageURL:str = obj["ImageURL"]
      """  ImageURL  """  
      self.Description:str = obj["Description"]
      """  Free form description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageLayerHeaderListTableset:
   def __init__(self, obj):
      self.ImageLayerHeaderList:list[Erp_Tablesets_ImageLayerHeaderListRow] = obj["ImageLayerHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImageLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.ImageID:str = obj["ImageID"]
      """  Name of image the individual layers are placed upon.  """  
      self.ImageURL:str = obj["ImageURL"]
      """  ImageURL  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.Description:str = obj["Description"]
      """  Free form description  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Approved:bool = obj["Approved"]
      """  When true, the definition can be assigned to a PcInput.  When flase, it cannot be assigned to a PcInput.  """  
      self.Version:int = obj["Version"]
      """  Internal number updated each time the definition is approved. This is used by Verify Configuration.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  ID of the person who approved the definition for use.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the definition was approved.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImageLayerTableset:
   def __init__(self, obj):
      self.ImageLayerHeader:list[Erp_Tablesets_ImageLayerHeaderRow] = obj["ImageLayerHeader"]
      self.ImageLayerDetail:list[Erp_Tablesets_ImageLayerDetailRow] = obj["ImageLayerDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtImageLayerTableset:
   def __init__(self, obj):
      self.ImageLayerHeader:list[Erp_Tablesets_ImageLayerHeaderRow] = obj["ImageLayerHeader"]
      self.ImageLayerDetail:list[Erp_Tablesets_ImageLayerDetailRow] = obj["ImageLayerDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportImageLayer_input:
   """ Required : 
   imageLayerID
   path
   fileName
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      """  Image Layer ID to be exported  """  
      self.path:str = obj["path"]
      self.fileName:str = obj["fileName"]
      pass

class ExportImageLayer_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageLayerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImageLayerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImageLayerTableset] = obj["returnObj"]
      pass

class GetListCustomHeadersWithDetail_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   customClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      self.customClause:str = obj["customClause"]
      """  Custom WhereClause  """  
      pass

class GetListCustomHeadersWithDetail_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageLayerHeaderListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImageLayerHeaderListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewImageLayerDetail_input:
   """ Required : 
   ds
   imageLayerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class GetNewImageLayerDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImageLayerHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      pass

class GetNewImageLayerHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseImageLayerHeader
   whereClauseImageLayerDetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseImageLayerHeader:str = obj["whereClauseImageLayerHeader"]
      self.whereClauseImageLayerDetail:str = obj["whereClauseImageLayerDetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImageLayerTableset] = obj["returnObj"]
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

class ImageLayerScriptCode_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class ImageLayerScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImageLayerUpdateScriptCode_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class ImageLayerUpdateScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportImageLayer_input:
   """ Required : 
   imageLayerID
   fileToImport
   imageURL
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      """  Image Layer ID to be imported  """  
      self.fileToImport:str = obj["fileToImport"]
      self.imageURL:str = obj["imageURL"]
      pass

class ImportImageLayer_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImageLayerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImageLayerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImageLayerTableset] = obj["ds"]
      pass

      """  output parameters  """  

